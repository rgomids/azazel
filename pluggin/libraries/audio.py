import os
import threading
import wave

import pyaudio
import speech_recognition as sr
from consts import AZAZEL_STONE


class Audio:
    def __init__(self, output_file=AZAZEL_STONE.OUTPUT_FILE):
        self.is_recording = False
        self.recognizer = sr.Recognizer()
        self.output_file = str(output_file)
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.chunk = 1024
        self.audio = pyaudio.PyAudio()
        self.thread = None

    @staticmethod
    def speak(text) -> None:
        """Função para converter texto em fala"""
        os.system(f'espeak "{text}"')

    def start_recording(self):
        print("Iniciando gravação...")
        self.thread = threading.Thread(target=self._record)
        self.thread.start()

    def stop_recording(self):
        print("Parando gravação...")
        self.thread.join()

    def _record(self, frames=[]):
        stream = self.audio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
        )

        while self.is_recording:
            data = stream.read(self.chunk)
            frames.append(data)

        # Parar e salvar o áudio
        print("Salvando gravação...")
        stream.stop_stream()
        stream.close()

        self._save(frames)

    def _save(self, frames):
        with wave.open(self.output_file, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.audio.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b"".join(frames))

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
