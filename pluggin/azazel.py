import gi
from consts import AZAZEL_STONE

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")


from consts import AZAZEL_STONE
from gi.repository import AppIndicator3, Gtk
from libraries.audio import Audio
from libraries.server import Server


class Azazel:
    def __init__(self):
        self.audio = Audio()
        self.server = Server()

        self.is_recording = False
        self.indicator = AppIndicator3.Indicator.new(
            "Azazel",
            f"{AZAZEL_STONE.IMAGES}/7V7.gif",
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS,
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

    def _make_llm_list(self):
        radio_group = []
        first_option = None
        for index, option_label in enumerate(AZAZEL_STONE.LLM_OPTIONS):
            if index == 0:
                radio_item = Gtk.RadioMenuItem.new_with_label(None, option_label)
                first_option = radio_item
            else:
                radio_item = Gtk.RadioMenuItem.new_with_label_from_widget(
                    first_option, option_label
                )

            radio_item.connect("toggled", self.on_option_toggled)
            radio_group.append(radio_item)
        return radio_group

    def _make_separator(self):
        separator = Gtk.SeparatorMenuItem()
        return separator

    def _make_record_button(self):
        # Botão de gravar/parar
        record_item = Gtk.MenuItem.new()
        record_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.record_icon = Gtk.Image.new_from_icon_name(
            "microphone-sensitivity-high", Gtk.IconSize.MENU
        )
        label = "Start Recording" if not self.is_recording else "Stop Recording"

        self.record_label = Gtk.Label(label=label)
        record_box.pack_start(self.record_icon, False, False, 0)
        record_box.pack_start(self.record_label, False, False, 5)
        record_item.add(record_box)
        record_item.connect("activate", self.on_record_toggle)
        return record_item

    def _make_quit_button(self):
        quit_item = Gtk.MenuItem.new_with_label("Quit")
        quit_item.connect("activate", self.on_quit)
        return quit_item

    def _make_sidebar(self):
        self.menu = Gtk.Menu()
        if not self.is_recording:
            radio_item = self._make_llm_list()
            for item in radio_item:
                self.menu.append(item)

            separator = self._make_separator()
            self.menu.append(separator)

        record_button = self._make_record_button()
        self.menu.append(record_button)

        separator = self._make_separator()
        self.menu.append(separator)

        # Item de sair
        if not self.is_recording:
            quit_item = self._make_quit_button()
            self.menu.append(quit_item)

        self.menu.show_all()

        self.indicator.set_menu(self.menu)

    def reload_sidebar(self):
        self.menu.destroy()
        self._make_sidebar()

    def on_quit(self):
        Gtk.main_quit()
        # TODO: parar tbmm o servidor go e fechar o programa

    def on_start(self):
        Gtk.main()

    def on_record_toggle(self, _):
        print("Iniciando a gravação...")
        if not self.is_recording:
            self.indicator.set_icon(f"{AZAZEL_STONE.IMAGES}/listening.gif")
            self.switch_record_state()
            self.reload_sidebar()
            self.audio.start_recording()
        else:
            self.switch_record_state()
            self.audio.stop_recording()
            self.indicator.set_icon(f"{AZAZEL_STONE.IMAGES}/7V7.gif")
            self.reload_sidebar()
            text = self.audio.transcribe_audio()
            response = self.server.ask_llm(text)
            self.audio.speak(response)
        pass

    def on_option_toggled(self, widget):
        if widget.get_active():
            self.server.change_llm(widget.get_label())

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
