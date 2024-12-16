import os
from pathlib import Path


class AZAZEL_STONE:
    DEAFULT_LANGUAGE = "pt-BR"
    FOLDER = Path().cwd()
    TEMP = "/var/tmp"
    PLUGGIN_PATH = FOLDER / "pluggin"
    OUTPUT_FILE = Path(f"{TEMP}/output.wav")
    IMAGES = PLUGGIN_PATH / "images"
    ACTIVATION_PHRASE = "Azazel"
    LLM_OPTIONS = ["Ollama Server", "GPT-4"]
    EGO = """ *** Answer as briefly as possible, without writing titles 
    or labels, in a way that doesn't sound like an AI response, but 
    rather how a grumpy man in his 40s would answer. Everything must
    be answered in English. If code is needed, leave it at the end of
    the 40s-style answer and separate it with "__code__" !!! *** """
