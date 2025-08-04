from model import list_models, chat_with_sealion

def main():
    print("=== SEA-LION Chat ===")

    try:
        models = list_models()
        model_ids = [m["id"] for m in models.get("data", [])]
    except Exception as e:
        print("Gagal ambil model:", e)
        return

    print("\nModel tersedia:")
    for i, model_id in enumerate(model_ids, start=1):
        print(f"{i}. {model_id}")

    selected = input("\nPilih model [tekan Enter untuk default]: ").strip()
    model_name = selected if selected else "aisingapore/Llama-SEA-LION-v2-8B-IT"

    while True:
        prompt = input("\nTanya (atau ketik 'exit'): ").strip()
        if prompt.lower() in ["exit", "quit"]:
            break
        try:
            output = chat_with_sealion(prompt, model=model_name)
            print("Jawaban:\n", output)
        except Exception as err:
            print("Gagal:", err)

if __name__ == "__main__":
    main()
