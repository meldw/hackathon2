# # model.py yang menggunakan Google Gemini API
# import os

# # Set API key untuk Gemini
# os.environ["GOOGLE_API_KEY"] = "GOOGLE_API_KEY"

# # Variabel global untuk Gemini
# gemini_model = None
# chat_session = None
# model_loaded = False

# # Fungsi untuk memuat model
# def load_model():
#     global gemini_model, chat_session, model_loaded
    
#     try:
#         # Import Google Generative AI dengan handling error yang lebih baik
#         try:
#             import google.generativeai as genai
#         except ImportError:
#             print("❌ Library google-generativeai tidak terinstall.")
#             print("Silakan install dengan perintah:")
#             print("pip install google-generativeai")
#             return False
        
#         # Konfigurasi dengan API key
#         api_key = os.environ.get("GOOGLE_API_KEY")
#         if not api_key:
#             print("❌ GOOGLE_API_KEY tidak ditemukan!")
#             return False
            
#         genai.configure(api_key=api_key)
        
#         # Inisialisasi model Gemini
#         print("Loading Gemini model...")
#         gemini_model = genai.GenerativeModel("gemini-1.5-flash")
#         chat_session = gemini_model.start_chat(history=[])
        
#         model_loaded = True
#         print("✅ Model Gemini berhasil dimuat!")
#         return True
#     except Exception as e:
#         print(f"❌ Error saat memuat model Gemini: {str(e)}")
#         return False

# # Fungsi untuk menghasilkan respons
# def generate_response(prompt, max_tokens=800):
#     global gemini_model, chat_session, model_loaded
    
#     # Coba load model jika belum
#     if not model_loaded:
#         success = load_model()
#         if not success:
#             return f"Model Gemini tidak bisa dimuat. Pastikan Anda telah menginstall library dengan 'pip install google-generativeai'. Pertanyaan Anda: {prompt}"
    
#     # Generate response
#     try:
#         response = chat_session.send_message(prompt)
#         return response.text
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return f"Terjadi kesalahan saat menghasilkan respons: {str(e)}"

# # Inisialisasi model saat import
# print("Initializing Gemini model...")
# try:
#     model_loaded = load_model()
# except Exception as e:
#     print(f"Fatal error loading model: {str(e)}")
#     print("Aplikasi akan tetap berjalan tetapi mungkin tidak bisa memberikan respons yang benar")

# # Print status untuk debugging
# print(f"Model module loaded successfully, model_loaded={model_loaded}")
