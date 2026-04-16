import os
from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")  # ✅ MUST ADD THIS
    )