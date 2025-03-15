import os
from importlib.metadata import files

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("ASSISTANT_ID")

client = OpenAI(api_key=key)

# Create vector store
vector_store = client.beta.vector_stores.create(name="PreguntasFrecuentes")
print(f"Vector Store ID: {vector_store.id}")

# Upload Preguntas Frecuentes files
file_paths = ["files/preguntas_frecuentes.txt"]
file_streams = [open(path, "rb") for path in file_paths]

# Add Files to Vector Store
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
    files=file_streams
)

# Check the status of files
print(f"File Status: {file_batch.status}")

# Update the assistant with a vector store
assistant = client.beta.assistants.update(
    assistant_id=assistant_id,
    tool_resources={
        "file_search": {
            "vector_store_ids": [
                vector_store.id
            ]
        }
    }
)
print("Assistant updated with vector store")

# Create a thread
thread = client.beta.threads.create()
print(f"Your thread id id - {thread.id}\n\n")

# Run a loop where user can ask questions
while True:
    text = input("What's your questions?\n")

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=text
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

    messages = list(client.beta.threads.messages.list(
        thread_id=thread.id,
        run_id=run.id,
    ))

    message_content = messages[0].content[0].text

    print("Response: \n")
    print(f"{message_content.value}\n")