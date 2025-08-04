import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("sk-E2RPMeO7POhBEXfs2_HF9w")
BASE_URL = "https://api.sea-lion.ai/v1"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "accept": "text/plain"
}

def list_models():
    url = f"{BASE_URL}/models"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()  # returns list of models

def chat_with_sealion(prompt, model="aisingapore/Llama-SEA-LION-v2-8B-IT", max_tokens=10):
    url = f"{BASE_URL}/chat/completions"
    payload = {
        "model": model,
        "max_completion_tokens": max_tokens,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.text.strip()
