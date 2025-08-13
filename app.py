from model import list_models, chat_with_sealion

def main():
    print("📢 Selamat datang di SEA-LION Chat CLI!")
    print("=======================================")

    try:
        models = list_models()
        model_ids = [m["id"] for m in models.get("data", [])]
    except Exception as e:
        print("❌ Gagal mengambil daftar model:", e)
        return

    print("\n📚 Model tersedia:")
    for i, model_id in enumerate(model_ids, start=1):
        print(f"  {i}. {model_id}")

    selected = input("\n👉 Pilih model (tekan Enter untuk default): ").strip()
    model_name = selected if selected else "aisingapore/Llama-SEA-LION-v3.5-8B-R"

    print("\n💬 Ketik pertanyaanmu. Ketik 'exit' untuk keluar.")
    print("-----------------------------------------------")

    while True:
        prompt = input("🧑 Kamu: ").strip()
        if prompt.lower() in ["exit", "quit"]:
            print("👋 Sampai jumpa!")
            break
        try:
            response = chat_with_sealion(prompt, model=model_name, max_tokens=300)
            print("🤖 SEA-LION:", response, "\n")
        except Exception as err:
            print("❌ Gagal mengambil jawaban:", err)

if __name__ == "__main__":
    main()
