import os

from sqlalchemy import create_engine

LLM_CONFIG_COLUMN = "llm model"
DEAFULT_LANGUAGE = "pt-BR"


class SPEACH_C:
    ACTIVATION_PHRASE = "Azazel"
    FAIL_TO_UNDERSTAND = "Não consegui entender o que você disse"


class DATABASE:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    ENGINE = create_engine(DATABASE_URL)
