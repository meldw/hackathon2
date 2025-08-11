# app.py
from flask import Flask, request, render_template_string
import os
import sys

# Import dengan handling error lebih baik
try:
    from model import generate_response
    print("✅ Model module berhasil diimport")
    has_model = True
except ImportError as e:
    has_model = False
    print(f"❌ Error importing model module: {e}")
    
    # Definisikan fungsi fallback jika model tidak bisa diimport
    def generate_response(prompt, max_tokens=100):
        return "Model tidak dapat diload. Pastikan Anda telah menginstall library: pip install google-generativeai"

app = Flask(__name__)
chat_history = []

@app.route("/", methods=["GET", "POST"])
def chat():
    global chat_history
    
    model_status = "Model tersedia" if has_model else "Model tidak tersedia"
    
    if request.method == "POST":
        user_input = request.form.get("message", "")
        if user_input:
            chat_history.append(("You", user_input))
            bot_reply = generate_response(user_input)
            chat_history.append(("AI", bot_reply))

    return render_template_string("""
        <html>
            <head>
                <title>AI Chatbot</title>
                <style>
                    body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                    .chat-container { margin-top: 20px; max-height: 500px; overflow-y: auto; }
                    .user-message { background: #e6f7ff; padding: 10px; border-radius: 10px; margin: 5px 0; }
                    .bot-message { background: #f0f0f0; padding: 10px; border-radius: 10px; margin: 5px 0; }
                    .status { font-size: 12px; color: #666; margin-bottom: 10px; }
                    form { display: flex; margin-top: 20px; }
                    input[type="text"] { flex-grow: 1; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
                    input[type="submit"] { margin-left: 10px; padding: 10px 20px; background: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; }
                    .header { display: flex; justify-content: space-between; align-items: center; }
                    .clear-button { background: #f44336; color: white; border: none; padding: 5px 10px; border-radius: 5px; cursor: pointer; }
                </style>
            </head>
            <body>
                <div class="header">
                    <h2>🤖 AI Chatbot dengan Gemini API</h2>
                    <form method="post" action="/clear" style="margin: 0;">
                        <button type="submit" class="clear-button">Clear Chat</button>
                    </form>
                </div>
                <div class="status">Status: {{ model_status }}</div>
                <form method="post">
                    <input type="text" name="message" placeholder="Type a message..." required>
                    <input type="submit" value="Send">
                </form>
                <div class="chat-container">
                    {% for role, msg in history %}
                        <div class="{{ 'user-message' if role == 'You' else 'bot-message' }}">
                            <strong>{{ role }}:</strong> {{ msg }}
                        </div>
                    {% endfor %}
                </div>
            </body>
        </html>
    """, history=chat_history, model_status=model_status)

@app.route("/clear", methods=["POST"])
def clear_chat():
    global chat_history
    chat_history = []
    return chat()
if __name__ == "__main__":
    print("Starting AI Chatbot...")
    app.run(debug=True, port=8080)  # Ubah port dari 5000 ke 8080 


    


