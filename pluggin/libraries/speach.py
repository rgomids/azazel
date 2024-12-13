import os

import speech_recognition as sr
from libraries.base.audio import Audio
from consts import AZAZEL_STONE


class Speach(Audio):
    def __init__(self, output_file=f"{AZAZEL_STONE.TEMP}/output.wav"):
        self.recognizer = sr.Recognizer()
        super().__init__(output_file)

    @staticmethod
    def speak(text) -> None:
        """Função para converter texto em fala"""
        os.system(f'espeak "{text}"')

    def transcribe_audio(self):
        with sr.AudioFile(self.output_file) as source:
            print("Carregando áudio...")
            audio_data = self.recognizer.record(source)

        try:
            print("Transcrevendo áudio...")
            text = self.recognizer.recognize_google(audio_data, language="pt-BR")
            print("Transcrição concluída!")
            return text
        except sr.UnknownValueError:
            print("O áudio não pôde ser entendido.")
            return None
        except sr.RequestError as e:
            print(f"Erro ao acessar o serviço de reconhecimento: {e}")
            return None
