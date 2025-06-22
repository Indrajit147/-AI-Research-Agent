📘 Smart Info Assistant
An intelligent summarization assistant that combines Wikipedia and web search to generate rich, structured summaries on any topic.

<!-- optional demo gif -->

🔍 What It Does
🧠 Uses OpenAI’s GPT-4o-mini to generate long, informative summaries

🌐 Combines data from Wikipedia and DuckDuckGo search

📄 Returns structured output (topic, summary, sources, tools used)

💾 Saves results to markdown or text files

🖥️ Use it in CLI or as a Streamlit web app

🚀 Demo (Streamlit UI)


🛠️ Features
📚 Accurate web and wiki integration

✅ Pydantic validation for safe, structured output

📦 Modular: clean separation of tools.py, main.py, and app.py

🧼 Handles noisy web data with cleaning & error handling

🧑‍💻 Developer-friendly CLI + beautiful UI

🧪 Tech Stack
LangChain

OpenAI GPT-4o

DuckDuckGo Search API

Streamlit

Pydantic

Rich

🧰 Installation
bash
Copy
Edit
git clone https://github.com/yourusername/smart-info-assistant.git
cd smart-info-assistant
pip install -r requirements.txt
Add your OpenAI API key to a .env file:

ini
Copy
Edit
OPENAI_API_KEY=your_key_here
🧑‍💻 Usage
🔧 Run CLI version:
bash
Copy
Edit
python main.py
🌐 Run Streamlit UI:
bash
Copy
Edit
streamlit run app.py
📁 Project Structure
bash
Copy
Edit
smart-info-assistant/
├── main.py           # CLI version
├── app.py            # Streamlit UI
├── tools.py          # Modular tools
├── .env              # API keys
├── requirements.txt  # Dependencies
└── research_*.md     # Saved outputs
✅ Example Output
Query: COVID-19 impact in Bangladesh

markdown
Copy
Edit
# 📌 Topic: COVID-19 impact in Bangladesh

## 🧾 Summary
Bangladesh faced significant health, social, and economic impacts during the COVID-19 pandemic. Lockdowns, overwhelmed hospitals, and vaccine rollouts shaped national response efforts. NGOs played a major role. The economy suffered during early lockdowns but saw gradual recovery post-2021...

## 📚 Sources
- Wikipedia: COVID-19 in Bangladesh
- bdnews24.com
- World Bank COVID Dashboard

## 🧰 Tools Used
- wikipedia
- search
💡 Ideas to Extend
Add YouTube/Arxiv scraping tools

Export to PDF or Notion

Track saved queries and search history

Deploy on Streamlit Cloud or HuggingFace Spaces

📜 License
MIT License — free to use, improve, and share

