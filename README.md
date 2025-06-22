<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Smart Info Assistant</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 2rem auto;
      max-width: 800px;
      line-height: 1.6;
      background: #f9f9f9;
      color: #333;
      padding: 1rem;
    }
    h1, h2, h3 {
      color: #1a73e8;
    }
    code, pre {
      background-color: #eee;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }
    .tag {
      background-color: #cce5ff;
      color: #004085;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.9em;
    }
    .code-block {
      background: #272822;
      color: #f8f8f2;
      padding: 1em;
      border-radius: 8px;
      overflow-x: auto;
      font-family: monospace;
    }
  </style>
</head>
<body>

  <h1>📘 Smart Info Assistant</h1>
  <p><em>An intelligent summarization assistant that combines Wikipedia and web search to generate rich, structured summaries on any topic.</em></p>

  <h2>🔍 What It Does</h2>
  <ul>
    <li>🧠 Uses <strong>OpenAI GPT-4o-mini</strong> to generate detailed summaries</li>
    <li>🌐 Combines data from <strong>Wikipedia</strong> and <strong>DuckDuckGo</strong></li>
    <li>📄 Returns structured output: topic, summary, sources, tools used</li>
    <li>💾 Supports saving results to markdown or text files</li>
    <li>🖥️ Available as CLI app and Streamlit web app</li>
  </ul>

  <h2>🛠️ Features</h2>
  <ul>
    <li>📚 Accurate data from web and Wikipedia</li>
    <li>✅ Pydantic validation ensures structured output</li>
    <li>📦 Modular: clean separation of components</li>
    <li>🧼 Cleans noisy web data automatically</li>
    <li>🧑‍💻 Developer-friendly and extensible</li>
  </ul>

  <h2>🧪 Tech Stack</h2>
  <ul>
    <li>LangChain</li>
    <li>OpenAI GPT-4o</li>
    <li>DuckDuckGo Search API</li>
    <li>Streamlit</li>
    <li>Pydantic</li>
    <li>Rich</li>
  </ul>

  <h2>🧰 Installation</h2>
  <pre class="code-block">
git clone https://github.com/yourusername/smart-info-assistant.git
cd smart-info-assistant
pip install -r requirements.txt
  </pre>

  <p>Create a <code>.env</code> file:</p>
  <pre class="code-block">
OPENAI_API_KEY=your_openai_api_key
  </pre>

  <h2>🧑‍💻 Usage</h2>
  <h3>🔧 CLI Version:</h3>
  <pre class="code-block">python main.py</pre>

  <h3>🌐 Streamlit Web App:</h3>
  <pre class="code-block">streamlit run app.py</pre>

  <h2>📁 Project Structure</h2>
  <pre class="code-block">
smart-info-assistant/
├── main.py           # CLI version
├── app.py            # Streamlit UI
├── tools.py          # Tools and utilities
├── .env              # API keys
├── requirements.txt  # Dependencies
└── research_*.md     # Output files
  </pre>

  <h2>✅ Example Output</h2>
  <pre class="code-block">
# 📌 Topic: COVID-19 impact in Bangladesh

## 🧾 Summary
Bangladesh faced significant health, social, and economic impacts during the COVID-19 pandemic. Lockdowns, overwhelmed hospitals, and vaccine rollouts shaped national response efforts...

## 📚 Sources
- Wikipedia: COVID-19 in Bangladesh
- bdnews24.com
- World Bank COVID Dashboard

## 🧰 Tools Used
- wikipedia
- search
  </pre>

  <h2>💡 Ideas to Extend</h2>
  <ul>
    <li>Add support for YouTube and ArXiv</li>
    <li>Export to PDF or Notion</li>
    <li>Deploy to Streamlit Cloud or HuggingFace Spaces</li>
  </ul>

  <h2>📜 License</h2>
  <p>MIT License — free to use, improve, and share.</p>

</body>
</html>
