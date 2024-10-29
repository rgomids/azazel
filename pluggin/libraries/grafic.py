import os
import tkinter as tk

from PIL import Image, ImageSequence, ImageTk


class Grafic:

    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def show_listening_gif(self):
        global gif_label, gif_frames
        gif_label.pack()
        gif_label.lift()
        self.animate_gif(0)

    def hide_listening_gif():
        global gif_label
        gif_label.pack_forget()

    def animate_gif(frame_index):
        global gif_label, gif_frames
        gif_label.config(image=gif_frames[frame_index])
        frame_index = (frame_index + 1) % len(gif_frames)
        # if gif_label.winfo_ismapped():
        #     gif_label.after(50, animate_gif, frame_index)

    def load_gif():
        global gif_frames, gif_label
        gif_path = os.path.expanduser("./listening.gif")
        gif = Image.open(gif_path)
        gif_frames = [
            ImageTk.PhotoImage(frame.copy().convert("RGBA"))
            for frame in ImageSequence.Iterator(gif)
        ]
        gif_label = tk.Label(image=gif_frames[0], bg="white")

    def start_casting(self):
        self.load_gif()
