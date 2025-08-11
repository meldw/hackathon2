
# model.py
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

tokenizer = None
model = None

def load_model():
    """Load model SEA-LION sekali saja"""
    global tokenizer, model
    if tokenizer is not None and model is not None:
        return  # sudah pernah load

    print("🔄 Loading SEA-LION model...")
    tokenizer = AutoTokenizer.from_pretrained(
        "aisingapore/Llama-SEA-LION-v3.5-8B-R",
        use_auth_token=HF_TOKEN
    )
    model = AutoModelForCausalLM.from_pretrained(
        "aisingapore/Llama-SEA-LION-v3.5-8B-R",
        device_map="auto",
        torch_dtype=torch.float16,
        load_in_4bit=True,  # ✅ Hemat RAM
        use_auth_token=HF_TOKEN
    )
    print("✅ Model loaded!")

def generate_responseee(prompt, max_new_tokens=200):
    """Generate chatbot response"""
    if tokenizer is None or model is None:
        raise ValueError("❌ Model belum dimuat! Panggil load_model() dulu.")

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_p=0.9,
        temperature=0.7
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    if response.startswith(prompt):
        response = response[len(prompt):].strip()
    return response.strip()



