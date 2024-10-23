import importlib

from loguru import logger


def build_class(class_name, **kwargs):
    try:
        class_obj = getattr(
            importlib.import_module(f"libraries.llm.{class_name.lower()}"),
            solve_class_name(class_name),
        )
        instance = class_obj(**kwargs)
        return instance
    except Exception as error:
        logger.error(f"Error building {solve_class_name(class_name.lower())}")
        logger.error(error)
        return None


def solve_class_name(string):
    return string[0].upper() + string[1:] + "Api"
