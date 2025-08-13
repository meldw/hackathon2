import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SEA_LION_API_KEY")
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

def chat_with_sealion(prompt, model="aisingapore/Llama-SEA-LION-v3-70B-IT", max_tokens=10):
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
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    reply = tokenizer.decode(outputs[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    return reply.strip()
