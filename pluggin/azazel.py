import speech_recognition as sr
import openai
import os
import json
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Caminho para o arquivo de configuração
config_file = os.path.expanduser("~/.config/azazel/config.json")

# Função para carregar a chave da API a partir do arquivo de configuração
def load_api_key():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)
            return config.get('api_key', '')
    return ''

# Função para salvar a chave da API no arquivo de configuração
def save_api_key(api_key):
    os.makedirs(os.path.dirname(config_file), exist_ok=True)
    with open(config_file, 'w') as f:
        json.dump({'api_key': api_key}, f)

# Função para configurar a chave da API
def configure_api_key():
    api_key = input("Por favor, insira sua chave de API da OpenAI: ")
    save_api_key(api_key)
    openai.api_key = api_key

# Carregar a chave da API ao iniciar
openai.api_key = load_api_key()
if not openai.api_key:
    configure_api_key()

# Função para converter texto em fala
def speak(text):
    os.system(f'espeak "{text}"')

# Função para reconhecer a fala
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Azazel está ouvindo...")
        show_listening_gif()
        audio = recognizer.listen(source)
    try:
        hide_listening_gif()
        text = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você: {text}")
        return text
    except sr.UnknownValueError:
        hide_listening_gif()
        return "Não consegui entender o que você disse"
    except sr.RequestError as e:
        hide_listening_gif()
        return f"Erro ao solicitar resultados; {e}"

# Função para consultar a API do ChatGPT
def ask_chatgpt(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Função de ativação por voz
def activate_voice_assistant():
    activation_phrase = "Olá Azazel"
    while True:
        command = recognize_speech()
        if activation_phrase.lower() in command.lower():
            os.system('notify-send "Azazel" "Como posso ajudar?"')
            speak("Como posso ajudar?")
            break

# Funções para mostrar e esconder o GIF
def show_listening_gif():
    global gif_label, gif_frames
    gif_label.pack()
    gif_label.lift()
    animate_gif(0)

def hide_listening_gif():
    global gif_label
    gif_label.pack_forget()

def animate_gif(frame_index):
    global gif_label, gif_frames
    gif_label.config(image=gif_frames[frame_index])
    frame_index = (frame_index + 1) % len(gif_frames)
    if gif_label.winfo_ismapped():
        gif_label.after(50, animate_gif, frame_index)

# Carregar o GIF
def load_gif():
    global gif_frames, gif_label
    gif_path = os.path.expanduser("./listening.gif")
    gif = Image.open(gif_path)
    gif_frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]
    gif_label = tk.Label(image=gif_frames[0], bg="white")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    load_gif()

    while True:
        print("1. Usar assistente")
        print("2. Configurar chave da API")
        choice = input("Escolha uma opção: ")
        if choice == '1':
            activate_voice_assistant()
            while True:
                question = input("Você: ")
                response = ask_chatgpt(question)
                print(f"Azazel: {response}")
                speak(response)
        elif choice == '2':
            configure_api_key()
        else:
            print("Opção inválida. Tente novamente.")
