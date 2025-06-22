import streamlit as st
import os
import re
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError
from tools import search_tool, wiki_tool, save_tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

# Load key
load_dotenv()

# Response format
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=1000)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an intelligent summarizer.
        Combine information from Wikipedia and Web Search.
        Summarize the query in detailed, clean, readable text.
        Output only JSON:
        {format_instructions}
        """
    ),
    ("human", "{query}"),
    ("ai", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# UI
st.set_page_config(page_title="📘 Smart Info Assistant")
st.title("📘 Smart Info Assistant")
st.markdown("Get a well-researched summary based on Wikipedia and Web Search")

query = st.text_input("🔍 What do you want to know?")

if st.button("Get Summary") and query:
    with st.spinner("Thinking..."):
        raw_response = executor.invoke({"query": query})
        raw_output = raw_response.get("output", "")

        # Clean
        if raw_output.startswith("```"):
            raw_output = re.sub(r"^```[a-z]*\n?", "", raw_output)
            raw_output = raw_output.rstrip("```").strip()
        raw_output = re.sub(r"//.*", "", raw_output)

        try:
            parsed = parser.parse(raw_output)

            st.markdown(f"### 📌 Topic\n{parsed.topic}")
            st.markdown(f"### 🧾 Summary\n{parsed.summary}")
            st.markdown("### 📚 Sources")
            for s in parsed.sources:
                st.markdown(f"- {s}")
            st.markdown("### 🧰 Tools Used")
            for t in parsed.tools_used:
                st.markdown(f"- {t}")

            # Optional Save
            if st.button("💾 Save to Markdown"):
                file = f"research_{parsed.topic.lower().replace(' ', '_')}.md"
                with open(file, "w", encoding="utf-8") as f:
                    f.write(f"# 📌 Topic: {parsed.topic}\n\n")
                    f.write(f"## 🧾 Summary\n{parsed.summary}\n\n")
                    f.write("## 📚 Sources\n")
                    for src in parsed.sources:
                        f.write(f"- {src}\n")
                    f.write("## 🧰 Tools Used\n")
                    for tool in parsed.tools_used:
                        f.write(f"- {tool}\n")
                st.success(f"Saved to {file}")

        except ValidationError as e:
            st.error(f"Failed to parse structured output:\n{e}")
            st.code(raw_output)
