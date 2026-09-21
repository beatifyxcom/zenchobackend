import os
from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not set")

client = genai.Client(api_key=api_key)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message", "")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=message
    )

    return jsonify({"answer": response.text})

@app.route("/")
def home():
    return "ZenchoAI Backend is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)