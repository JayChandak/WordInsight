# core/llm_client.py
import os
import requests
import streamlit as st

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def get_words_from_groq(category: str) -> str:
    """Fetches 10 words with definitions from Groq LLM and returns raw string."""
    if not GROQ_API_KEY:
        return "Error: GROQ_API_KEY not found. Check your .env file."

    prompt = (
    f"List exactly 10 unique words related to '{category}', "
    f"each followed by a colon and a 1 or 2 line definition. "
    f"Output strictly as:\n"
    f"Word1: Definition\nWord2: Definition\n...Word10: Definition"    
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    data = response.json()

    print("Groq API Response:", data)  # Debug

    choices = data.get("choices")
    if not choices:
        return "Error: " + data.get("error", {}).get("message", "Unknown error")

    return choices[0].get("message", {}).get("content", choices[0].get("text", ""))
