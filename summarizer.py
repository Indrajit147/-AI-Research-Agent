import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from rich import print as rprint

# Load OpenAI key
load_dotenv()

# Step 1: Search tool to gather multiple snippets
search_tool = DuckDuckGoSearchRun()

def gather_snippets(query: str, num_snippets: int = 5) -> list[str]:
    raw_results = search_tool.run(query)
    # Simple split based on dots if it's a giant string (DuckDuckGo returns one string)
    snippets = raw_results.split('. ')
    return snippets[:num_snippets]

# Step 2: LLM for summarization
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_tokens=1000)

summary_prompt = ChatPromptTemplate.from_template("""
You are a smart assistant.
Given a list of raw web snippets, write a comprehensive and informative summary.

Snippets:
{snippets}

Instructions:
- Do NOT copy directly.
- Combine info logically and clearly.
- Be accurate, detailed, and readable.

Return only the summary.
""")

def generate_summary_from_snippets(snippets: list[str]) -> str:
    full_snippet_block = "\n- " + "\n- ".join(snippets)
    prompt_value = summary_prompt.invoke({"snippets": full_snippet_block})
    return llm.invoke(prompt_value).content

# Entry point
if __name__ == "__main__":
    user_query = input("🔍 What topic do you want a detailed summary on? ")

    print("\n🌐 Gathering search results...")
    snippets = gather_snippets(user_query)

    if not snippets:
        print("❌ No snippets found.")
        exit()

    print("\n🤖 Generating summary...")
    summary = generate_summary_from_snippets(snippets)

    rprint("\n[bold green]🧾 Summary:[/]")
    rprint(summary)

    save_option = input("\n💾 Save to file? (y/n): ").lower()
    if save_option == "y":
        filename = f"search_summary_{user_query.lower().replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# 📌 Topic: {user_query}\n\n")
            f.write("## 🧾 Summary\n")
            f.write(summary)
        rprint(f"\n✅ Saved to [bold]{filename}[/bold]")
