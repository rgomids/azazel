from typing import Union

from consts import CONSTANTS as ct
from helpers.builder import build_class
from libraries.grafic import Grafic
from libraries.llm import GPTApi, OllamaApi
from libraries.speach import Speach


class Azazel:
    def __init__(self):
        self.speach = Speach()
        self.grafic = Grafic()
        self.llm = self._get_llm_class()
        self._prepare_images(False)

    def _get_llm_class(self) -> Union[OllamaApi, GPTApi]:
        for key, value in enumerate(ct.LLM_OPTIONS.values()):
            print(f"{key + 1}. {value}")
        option = int(input("Escolha uma opção: "))
        return build_class(ct.LLM_OPTIONS[option])

    def _prepare_images(self, use_graffics: bool = True):
        if use_graffics:
            self.grafic.start_casting()

    def run(self):
        self.speach._speak("Como posso ajudar?")
        while True:
            question = self.speach.received_speach()
            response = self.llm.ask_llm(question)
            print(f"Azazel: {response}")
            self.speach.speak(response)


if __name__ == "__main__":
    a = Azazel()
    a.run()
