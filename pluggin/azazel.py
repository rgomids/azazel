import os

import gi
from consts import AZAZEL_STONE

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")


from consts import AZAZEL_STONE
from gi.repository import AppIndicator3
from libraries.audio import Audio
from libraries.grafic import Grafic
from libraries.server import Server


class Azazel(Grafic):
    def __init__(self):
        super().__init__()
        self.audio = Audio()
        self.server = Server()

        self.indicator = AppIndicator3.Indicator.new(
            "Azazel",
            f"{AZAZEL_STONE.IMAGES}/7V7.gif",
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS,
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

    def _make_sidebar(self):
        super()._make_sidebar()
        self.indicator.set_menu(self.menu)

    def on_quit(self, _):
        super().on_quit()
        os._exit(0)

    def on_record_toggle(self, _):
        print("Iniciando a gravação...")
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()
            self.create_anwser()

    def on_option_toggled(self, widget):
        if widget.get_active():
            self.server.change_llm(widget.get_label())

    def start_recording(self):
        self.indicator.set_icon(f"{AZAZEL_STONE.IMAGES}/listening.gif")
        self.switch_record_state()
        self.reload_sidebar()
        self.audio.start_recording()

    def stop_recording(self):
        self.indicator.set_icon(f"{AZAZEL_STONE.IMAGES}/7V7.gif")
        self.switch_record_state()
        self.audio.stop_recording()
        self.reload_sidebar()

    def create_anwser(self):
        text = self.audio.transcribe_audio()
        response = self.server.ask_llm(text)
        if AZAZEL_STONE.USE_VOICE:
            self.audio.speak(response)

    def switch_record_state(self):
        if self.is_recording:
            self.audio.is_recording = False
            self.is_recording = False
        else:
            self.audio.is_recording = True
            self.is_recording = True

    def run(self):
        self._make_sidebar()
        self.on_start()


if __name__ == "__main__":
    a = Azazel()
    a.run()
