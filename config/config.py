import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath("__file__"))
base_dir = os.path.dirname(current_dir)
env_path = os.path.join(base_dir, "api.env")
load_dotenv(env_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")