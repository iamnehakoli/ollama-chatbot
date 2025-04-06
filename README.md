# 🦙 Simple Ollama Chatbot (Streamlit + LangChain + Ollama)

This is a basic web application built with **Streamlit** that allows you to interact directly with a **local Ollama language model** (e.g., `llama3.1:8b`) using **LangChain**.

It provides a clean interface to enter a prompt and view the model's response. This version does **not use agents** — it simply invokes the base model's capabilities.

---

## Prerequisites

Before you begin, ensure the following are installed and running:

- **Python** ≥ 3.8  
- **pip** (Python package installer)  
- **Ollama** – [Download & install here](https://ollama.com/)  
- **Ollama Model** – This example uses `llama3.1:8b`. Pull the model using:

```bash
ollama pull llama3.1:8b
```
⚠️ Make sure Ollama is installed and actively running when you use the app.

## Installation

Clone the repository and install the required Python libraries:
```bash
git clone https://github.com/iamnehakoli/ollama-chatbot.git
cd ollama-chatbot
pip install -r requirements.txt
```

## Run the application
```bash
streamlit run main.py
```
