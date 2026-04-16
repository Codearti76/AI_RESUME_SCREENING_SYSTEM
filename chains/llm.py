import os
from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(
        model="llama3-70b-8192",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")  # ✅ MUST ADD THIS
    )