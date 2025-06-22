import os
import re
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool
from rich import print as rprint

# Load API key
load_dotenv()

# Define structured schema
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# LLM with longer output
llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=1000)

# Output parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Prompt instructing to use multiple sources
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an intelligent summarization agent.
        Use all available tools (Wikipedia and Web Search).
        Combine their information into a DETAILED, INFORMATIVE summary.
        Return the final response in JSON format only:
        {format_instructions}
        """
    ),
    ("human", "{query}"),
    ("ai", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Query input
query = input("🔍 Enter your research topic: ")
print("\n🤖 Thinking...\n")
raw_response = agent_executor.invoke({"query": query})

# Parse response
try:
    raw_output = raw_response.get("output", "")
    if raw_output.startswith("```"):
        raw_output = re.sub(r"^```[a-z]*\n?", "", raw_output)
        raw_output = raw_output.rstrip("```").strip()
    raw_output = re.sub(r"//.*", "", raw_output)

    structured_response = parser.parse(raw_output)

    # Display nicely
    rprint("[bold cyan]📌 Topic:[/]", structured_response.topic)
    rprint("[bold green]🧾 Summary:[/]", structured_response.summary)
    rprint("[bold yellow]📚 Sources:[/]", structured_response.sources)
    rprint("[bold magenta]🧰 Tools Used:[/]", structured_response.tools_used)

    # Save markdown
    safe_title = structured_response.topic.lower().replace(" ", "_")
    filename = f"research_{safe_title}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# 📌 Topic: {structured_response.topic}\n\n")
        f.write(f"## 🧾 Summary\n{structured_response.summary}\n\n")
        f.write("## 📚 Sources\n")
        for source in structured_response.sources:
            f.write(f"- {source}\n")
        f.write("## 🧰 Tools Used\n")
        for tool in structured_response.tools_used:
            f.write(f"- {tool}\n")
    rprint(f"\n✅ Saved to: [bold]{filename}[/bold]")

except Exception as e:
    print("❌ Parsing failed:", e)
    print("📄 Raw:", raw_response)
