import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

def get_llm():
    """Initializes the LLM configured via Fireworks AI for Kimi 2.6"""
    return init_chat_model(
        model="accounts/fireworks/models/kimi-k2p6",
        model_provider="fireworks",
        temperature=0.0,
        fireworks_api_key=os.getenv("FIREWORKS_API_KEY", "")
    )
