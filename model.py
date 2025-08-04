from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model & tokenizer
tokenizer = AutoTokenizer.from_pretrained("aisingapore/Llama-SEA-LION-v2-8B-IT")
model = AutoModelForCausalLM.from_pretrained("aisingapore/Llama-SEA-LION-v2-8B-IT")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def chat_with_model(message, max_new_tokens=100):
    """
    Mengirim pesan ke model SEA-LION dan mengembalikan respons.
    """
    messages = [{"role": "user", "content": message}]

    inputs = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=True,
        return_dict=True,
        return_tensors="pt"
    ).to(device)

    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True)

    return response
