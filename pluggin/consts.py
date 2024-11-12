import os

from dotenv import load_dotenv
from sqlmodel import create_engine

DEFAULT_LLM = "ollama"
LLM_CONFIG_COLUMN = "llm model"


class SPEACH_C:
    ACTIVATION_PHRASE = "Demonio"
    FAIL_TO_UNDERSTAND = "Não consegui entender o que você disse"


class DATABASE:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    ENGINE = create_engine(DATABASE_URL)
