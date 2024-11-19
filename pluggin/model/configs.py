from consts import DATABASE
from sqlalchemy import text


def get_llm():
    with DATABASE.ENGINE.connect() as connection:
        result = connection.execute(
            text("SELECT value FROM configs WHERE config_name = 'llm_model';")
        ).fetchone()

    return result[0]
