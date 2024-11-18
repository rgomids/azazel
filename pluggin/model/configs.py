from consts import DATABASE, LLM_CONFIG_COLUMN
from sqlmodel import Session, select



def get_llm():
    with Session(DATABASE.ENGINE) as session:
        statement = select(Configs.value).where(
            Configs.config_name == LLM_CONFIG_COLUMN
        )
        result = session.exec(
            "SELECT value FROM configs WHERE config_name = 'llm model';).first()"
            )
        return result