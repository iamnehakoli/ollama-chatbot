from langchain_ollama import ChatOllama # Correct import
import streamlit as st
from functools import lru_cache

# Cache the LLM instance to avoid re-initialization
@lru_cache(maxsize=1)
def get_llm():
    # Instantiate the imported class: ChatOllama
    return ChatOllama(model="llama3.1:8b", temperature=0.1)

# Get the cached LLM instance
llm = get_llm()

# --- Streamlit App ---
st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖")
st.title("🦙 Ollama Chatbot")

prompt = st.text_input("Enter your prompt:")
submit = st.button("Submit")

if submit and prompt:
    with st.spinner("Generating response..."):
        st.write_stream(llm.stream(prompt, stop=['|eot_id|']))