from dotenv import load_dotenv
import os
load_dotenv()


## configuración del la api

HOST="localhost" ## 127.0.0.0
PORT=8082
DEBUG=True

# ESTE UN COMENTARIO
"""
Configuración del modelo
"""

OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
GPT_MODEL="gpt-3.5-turbo-1106"
TEMPERATURE=0.7
MAX_TOKENS=100
