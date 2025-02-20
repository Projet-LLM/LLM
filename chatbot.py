from fastapi import FastAPI, HTTPException
from chatbot import chatbot
import mistral 
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
mistral_api_key = os.getenv("MISTRAL_API_KEY")
mistral_client = mistral.Client(mistral_api_key)


@app.get("/ask")
def chat(prompt: str):

    response = mistral_client.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=150
    )
    return {"response": response.generations[0].text.strip()}