import json
from functools import wraps

from loguru import logger
from requests.exceptions import ConnectionError
from utils.exception import InvalidResponseError


def handle_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()

            if response.json()["response"] != "Ok":
                raise InvalidResponseError(
                    f"Response field indicates failure: {data['response']}"
                )
            return response

        except ConnectionError:
            logger.error("Connection Error... Is server running?")

    return wrapper
