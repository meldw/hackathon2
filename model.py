import os
import requests
from dotenv import load_dotenv

# Load variabel lingkungan dari file .env
load_dotenv()

# Ambil API Key dari environment
API_KEY = os.getenv("sk-E2RPMeO7POhBEXfs2_HF9w")  # Ganti dengan key env-mu yang benar
BASE_URL = "https://api.sea-lion.ai/v1"

# Header standar untuk API SEA-LION
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "accept": "application/json"
}

def list_models():
    """Mengambil daftar model SEA-LION yang tersedia"""
    url = f"{BASE_URL}/models"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def chat_with_sealion(prompt, model="aisingapore/Llama-SEA-LION-v2-8B-IT", max_tokens=300):
    """Mengirim prompt dan mengembalikan balasan dari model"""
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
    result = response.json()
    
    # Ambil konten jawaban
    return result["choices"][0]["message"]["content"]
