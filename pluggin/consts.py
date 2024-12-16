import os
from pathlib import Path


class AZAZEL_STONE:
    DEAFULT_LANGUAGE = "pt-BR"
    FOLDER = Path().cwd()
    TEMP = " var/tmp"
    OUTPUT_FILE = Path(f"{TEMP}/output.wav")
    IMAGES = FOLDER / "images"
    ACTIVATION_PHRASE = "Azazel"
    FAIL_TO_UNDERSTAND = "Não consegui entender o que você disse"
    LLM_OPTIONS = ["Ollama Server", "GPT-4"]
