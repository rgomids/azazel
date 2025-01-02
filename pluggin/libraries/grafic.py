from consts import AZAZEL_STONE
from gi.repository import Gtk


class Grafic:
    def __init__(self):
        self.create_menu()
        self.is_recording = False

    def create_menu(self):
        self.menu = Gtk.Menu()

    def destroy_menu(self):
        self.menu.destroy()

    def reload_sidebar(self):
        self.destroy_menu()
        self.create_menu()
        self._make_sidebar()

    def _make_sidebar(self):
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

    def on_record_toggle(self, _):
        pass

    def on_record_toggle(self, _):
        pass

    def on_option_toggled(self, _):
        pass

    def on_quit(self, _):
        Gtk.main_quit()

    def on_start(self):
        Gtk.main()
