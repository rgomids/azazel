import speech_recognition as sr
from consts import CONSTANTS as cs


class Speach:
    def _speak(cls, text) -> None:
        """Função para converter texto em fala"""
        os.system(f'espeak "{text}"')

    def _notify(cls, text: str) -> None:
        os.system(f'notify-send "Azazel" {text}')

    # Função de ativação por voz
    def activate_voice_assistant(
        self, activation_phrase: str = cs.ACTIVATION_PHRASE
    ) -> None:
        command = self.recognize_speech()
        if activation_phrase.lower() in command.lower():
            # self._notify("Como posso ajudar?")
            self._speak("Como posso ajudar?")

    def recognize_speech(self) -> str:
        """Função para reconhecer a fala"""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Azazel está ouvindo...")
            show_listening_gif()
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você: {text}")
            return text
        except sr.UnknownValueError:
            return "Não consegui entender o que você disse"
        except sr.RequestError as e:
            return f"Erro ao solicitar resultados; {e}"
