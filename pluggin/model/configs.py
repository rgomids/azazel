from typing import Optional

from consts import DATABASE, DEFAULT_LLM, LLM_CONFIG_COLUMN
from sqlmodel import Field, Session, SQLModel, select


class Configs(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    config_name: str = Field(max_length=50)
    value: str = Field(default="", max_length=200)


def start_db():
    SQLModel.metadata.create_all(DATABASE.ENGINE)
    with Session(DATABASE.ENGINE) as session:
        new_config = Configs(config_name=LLM_CONFIG_COLUMN, value=DEFAULT_LLM)
        session.add(new_config)
        session.commit()


def get_llm():
    with Session(DATABASE.ENGINE) as session:
        statement = select(Configs.value).where(
            Configs.config_name == LLM_CONFIG_COLUMN
        )
        result = session.exec(statement).first()
        return result
