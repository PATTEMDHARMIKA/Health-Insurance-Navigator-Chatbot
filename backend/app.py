from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the Hugging Face model (flan-t5-base for better responses)
chatbot_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", framework="pt")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Structured prompt for clearer answers
        prompt = f"""You are a helpful assistant specialized in health insurance.
Answer the following question in simple, clear terms for a user:
Question: {user_input}
Answer:"""

        # Generate the response
        response = chatbot_pipeline(prompt, max_length=200, do_sample=True, temperature=0.7)
        reply = response[0]["generated_text"].strip()

    except Exception as e:
        reply = f"Sorry, I encountered an error: {str(e)}"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
