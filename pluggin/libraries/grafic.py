from consts import AZAZEL_STONE

from gi.repository import Gtk


class Grafic:
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
