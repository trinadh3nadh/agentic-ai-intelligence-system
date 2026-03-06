# 🤖 Agentic AI Intelligence System

An advanced **multi-agent AI platform** that combines **research agents, debate agents, autonomous reasoning, knowledge graphs, and data analysis** into a single interactive system.

This project demonstrates **Agentic AI architecture**, where multiple AI agents collaborate, reason, critique, and improve responses using modern LLM-based workflows.

Built using **Streamlit, Groq LLMs, Tavily Search, and Python AI tools**, the system showcases how autonomous AI agents can solve complex tasks.

---

# 🚀 Features

### 🔎 Research Agent

Searches the web and summarizes reliable information using an LLM.

### 🧠 Debate Agent

Generates **two different viewpoints** and synthesizes a balanced conclusion.

### 📊 Data Analyst Agent

Uploads datasets and automatically generates:

* statistical summaries
* visualizations
* AI insights

### 🕸 Knowledge Graph Agent

Extracts entities and relationships from text and builds **interactive knowledge graphs**.

### ⚙ Autonomous AI Agent

Plans tasks, executes tools, critiques answers, and improves responses automatically.

### 🤝 Collaborative AI Agents

Multiple agents collaborate to produce a **higher-quality final answer** through reasoning and synthesis.

### 📄 AI Report Generator

Allows users to **download AI-generated reports** for queries.

---

# 🏗 Architecture Overview

The system follows an **Agentic AI architecture** where different agents handle specific tasks.

```
User Query
    ↓
Planner Agent
    ↓
Tool Execution
    ↓
Research / Debate / Data Analysis
    ↓
Critic Agent
    ↓
Reflection Agent
    ↓
Synthesizer Agent
    ↓
Final Answer
```

This architecture demonstrates **AI agent orchestration**, a key concept in modern GenAI systems.

---

# 🧰 Tech Stack

### AI & LLM

* Groq API (Llama 3.1)
* Tavily Search API
* Sentence Transformers

### Data Science

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Knowledge Graphs

* NetworkX
* PyVis

### Framework

* Streamlit

### Deployment

* Streamlit Cloud
* GitHub

---

# 📂 Project Structure

```
agentic-ai-intelligence-system
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── agents
│   ├── research_agent.py
│   ├── debate_agent.py
│   ├── data_analyst_agent.py
│   ├── kg_agent.py
│   ├── planner_agent.py
│   ├── tool_executor.py
│   ├── critic_agent.py
│   ├── reflection_agent.py
│   └── synthesizer_agent.py
│
├── tools
│   └── web_search.py
│
├── utils
│   ├── llm.py
│   ├── model_loader.py
│   ├── report_generator.py
│   └── agent_timeline.py
│
└── .streamlit
    └── config.toml
```

---

# ⚡ Installation

Clone the repository:

```
git clone https://github.com/trinadh3nadh/agentic-ai-intelligence-system
cd agentic-ai-intelligence-system
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

# 🔑 API Keys Setup

This project requires two APIs:

* **Groq API** (LLM)
* **Tavily API** (web search)

Create a local secrets file:

```
.streamlit/secrets.toml
```

Add your keys:

```
GROQ_API_KEY="your_groq_api_key"
TAVILY_API_KEY="your_tavily_api_key"
```

⚠ **Never commit API keys to GitHub.**

---

# ☁ Deployment

This project can be deployed easily using **Streamlit Cloud**.

Steps:

1. Push the repository to GitHub
2. Go to **Streamlit Cloud**
3. Connect your repository
4. Set `app.py` as the entry file
5. Add API keys in **Streamlit Secrets**

---

# 🎯 Example Use Cases

* AI research assistant
* autonomous knowledge discovery
* data exploration tools
* multi-agent AI orchestration
* LLM-based analytics systems

---

# 👨‍💻 Author

**Trinadh Kolluboyina**

AI | ML Engineer | Data Scientist

---

# ⭐ Acknowledgements

* Groq AI
* Tavily Search
* Streamlit
* Open-source AI ecosystem

