# 🤖 AI Research Agent

An intelligent research assistant powered by LangChain, OpenAI GPT-4o-mini, and real-time tools like DuckDuckGo and Wikipedia. It performs multi-step research using agent-based reasoning and returns structured outputs with options to save results locally.

---

## 🧠 Features

- 🔍 Web search via DuckDuckGo  
- 📚 Wikipedia query integration  
- 📄 Structured response parsing using Pydantic  
- 🛠 Tool-calling agent via LangChain  
- 💾 Save research results to `.txt` with timestamp  
- 🔀 Easily switch between OpenAI and Anthropic models

---

## 🚀 How It Works

1. You provide a research query.
2. The agent uses tools like:
   - DuckDuckGo for live web search
   - Wikipedia for encyclopedic facts
   - A local file saver tool
3. The response is parsed into a structured format:
   - `topic`, `summary`, `sources`, `tools_used`
4. Final result is printed and optionally saved to a `.txt` file.

---

## 🧩 Project Structure
├── main.py # Agent setup and execution script
├── tools.py # Search, Wiki, and Save tools
├── .env # API keys and secrets
├── requirements.txt # Python dependencies
└── research_output.txt # File where results are saved

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-research-agent.git
cd ai-research-agent

### 1. Clone the Repository
### 2. Create and Activate a Virtual Environment

