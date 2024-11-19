import os

import speech_recognition as sr
from consts import DEAFULT_LANGUAGE
from consts import SPEACH_C as sc


class Speach:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    @staticmethod
    def speak(text) -> None:
        """Função para converter texto em fala"""
        os.system(f'espeak "{text}"')

    def _get_raw_audio(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Azazel está ouvindo...")
            return self.recognizer.listen(source)

    def _recognize_speech(self, audio) -> str:
        """Função para reconhecer a fala"""
        try:
            text = self.recognizer.recognize_google(audio, language=DEAFULT_LANGUAGE)
            print(f"Você: {text}")
            return text
        except sr.UnknownValueError:
            return sc.FAIL_TO_UNDERSTAND

    def received_speach(
        self,
        activation_phrase: str = sc.ACTIVATION_PHRASE,
    ) -> str:
        raw = self._get_raw_audio()
        command = self._recognize_speech(raw)
        if (
            command.lower().startswith(activation_phrase.lower())
            or activation_phrase.lower() in command.lower()
        ):
            return command[len(activation_phrase) :].strip()
