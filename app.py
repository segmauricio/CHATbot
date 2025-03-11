import os
from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")  # Ensure index.html is in a 'templates' folder

@app.route("/api", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("text", "")  # Match key from frontend

    if not user_message:
        return jsonify({"response": "No message provided"}), 400

    try:
        # ✅ New OpenAI API usage
        client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Pass API key to OpenAI client
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )

        bot_response = response.choices[0].message.content  # ✅ Updated way to access response
        return jsonify({"response": bot_response})

    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()



