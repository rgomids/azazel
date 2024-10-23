import json
import os
import tkinter as tk

import openai
import speech_recognition as sr
from PIL import Image, ImageSequence, ImageTk


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
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você: {text}")
        return text
    except sr.UnknownValueError:
        hide_listening_gif()
        return "Não consegui entender o que você disse"
    except sr.RequestError as e:
        hide_listening_gif()
        return f"Erro ao solicitar resultados; {e}"


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
    gif_frames = [
        ImageTk.PhotoImage(frame.copy().convert("RGBA"))
        for frame in ImageSequence.Iterator(gif)
    ]
    gif_label = tk.Label(image=gif_frames[0], bg="white")


if __name__ == "__main__":
    

from pluggin.libraries.gpt import GPTAPI
from pluggin.libraries.ollama import Ollama

class Azazel:
    def __init__(self):
        print("1. GPT")
        print("2. Lhamas")
        llm= input("Escolha uma opção: ")
        if llm == 1:
            self.llm  = GPTAPI()
        else:
            self.llm = Ollama()
        
    def run(self):
        root = tk.Tk()
        root.withdraw()
        load_gif()

        while True:
            activate_voice_assistant()
            while True:
                question = input("Você: ")
                response = self.llm.ask_llm(question)
                print(f"Azazel: {response}")
                speak(response)