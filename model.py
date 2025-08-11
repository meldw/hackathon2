# model.py
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

HF_TOKEN = st.secrets["HUGGINGFACE_TOKEN"]
MODEL_NAME = "aisingapore/Llama-SEA-LION-v3.5-8B-R"

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        token=HF_TOKEN,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    return tokenizer, model

tokenizer, model = load_model()

def generate_response(user_message, max_new_tokens=128):
    messages = [
        {"role": "user", "content": user_message}
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    ).to(model.device)

    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)

    reply = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)
    return reply.strip()
