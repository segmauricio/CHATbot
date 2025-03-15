import os
from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

@app.route("/")
def index():
    return render_template("index.html")  # Ensure index.html is in a 'templates' folder

@app.route("/api", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("text", "")

    if not user_message:
        return jsonify({"response": "No message provided"}), 400

    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Initialize client

        # Create a thread (required for assistants)
        thread = client.beta.threads.create()

        # Send message to the assistant
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )

        # Run the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID
        )

        # Poll for completion
        while run.status in ["queued", "in_progress"]:
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        # Get the latest message from the assistant
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        bot_response = messages.data[0].content[0].text.value  # Extract response text

        return jsonify({"response": bot_response})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run()



