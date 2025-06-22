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
├── main.py </br>
├── tools.pys</br>
├── .env</br>
├── requirements.txt </br>
└── research_output.txt </br>

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Indrajit147/AI-Research-Agent.git
cd ai-research-agent
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```
### 4. Set Up Environment Variables
```bash
OPENAI_API_KEY=your_openai_key
# ANTHROPIC_API_KEY=your_claude_key (optional)

```

### 🏃‍♂️ Run the Agent
```bash
python main.py

```
---
📄 License
MIT License. Feel free to modify or expand it for academic, commercial, or personal projects.
---

Indrajit Gupta</br>
Electronics & Communication Engineering @ KUET </br>
Project guided by OpenAI & LangChain tools
---
