# model.py
import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

load_dotenv()

token = st.secrets["HUGGINGFACE_TOKEN"]

tokenizer = AutoTokenizer.from_pretrained("aisingapore/Llama-SEA-LION-v2-8B-IT", token=token)
model = AutoModelForCausalLM.from_pretrained("aisingapore/Llama-SEA-LION-v2-8B-IT", token=token)

def generate_response(prompt, max_tokens=100):
    messages = [{"role": "user", "content": prompt}]
    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(**inputs, max_new_tokens=max_tokens)
    response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    return response.strip()
