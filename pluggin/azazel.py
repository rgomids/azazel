from threading import Thread
from typing import Union

import gi
from libraries.grafic import Grafic
from libraries.server import Server
from libraries.speach import Speach
from consts import AZAZEL_STONE

from libraries.base.plugin import Plugin

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")


class Azazel(Plugin):
    def __init__(self):

        self.speach = Speach()
        self.grafic = Grafic()
        self.server = Server()
        self.server.change_llm(AZAZEL_STONE.LLM_OPTIONS[0])
        super().__init__()

    def on_record_toggle(self, _):
        print("Iniciando a gravação...")
        if not self.speach.is_recording:
            self.speach.start_recording()
        else:
            self.speach.stop_recording()
            text = self.speach.transcribe_audio()
            response = self.server.ask_llm(text)
            self.speach.speak(response)

    def on_option_toggled(self, widget):
        if widget.get_active():
            self.server.change_llm(widget.get_label())


if __name__ == "__main__":
    a = Azazel()
