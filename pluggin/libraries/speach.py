import speech_recognition as sr


class Speach:  
    def speak(text):
        """Função para converter texto em fala"""
        os.system(f'espeak "{text}"')
        
    # Função de ativação por voz
    def activate_voice_assistant():
        activation_phrase = "Olá Azazel"
        while True:
            command = recognize_speech()
            if activation_phrase.lower() in command.lower():
                os.system('notify-send "Azazel" "Como posso ajudar?"')
                speak("Como posso ajudar?")
                break

    def recognize_speech():
        """Função para reconhecer a fala"""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Azazel está ouvindo...")
            show_listening_gif()
            audio = recognizer.listen(source)
        try:
            hide_listening_gif()
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você: {text}")
            return text
        except sr.UnknownValueError:
            hide_listening_gif()
            return "Não consegui entender o que você disse"
        except sr.RequestError as e:
            hide_listening_gif()
            return f"Erro ao solicitar resultados; {e}"