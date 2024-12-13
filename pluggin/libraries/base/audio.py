import threading
import wave

import pyaudio


class Audio:
    def __init__(self, output_file):
        self.output_file = output_file
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.chunk = 1024
        self.audio = pyaudio.PyAudio()
        self.is_recording = False
        self.thread = None

    def start_recording(self):
        print("Iniciando gravação...")
        self.is_recording = True
        self.thread = threading.Thread(target=self._record)
        self.thread.start()

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

    def stop_recording(self):
        print("Parando gravação...")
        self.is_recording = False
        self.thread.join()
