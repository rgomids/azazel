import os

from sqlalchemy import create_engine

LLM_CONFIG_COLUMN = "llm model"
DEAFULT_LANGUAGE = "pt-BR"


class SPEACH_C:
    ACTIVATION_PHRASE = "Demonio"
    FAIL_TO_UNDERSTAND = "Não consegui entender o que você disse"
    BASIC_HEADER_REQUEST = (
        "Crie uma resposta curta para a pergunta abaixo, seja o mais sucinto possível"
    )


class DATABASE:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    ENGINE = create_engine(DATABASE_URL)
