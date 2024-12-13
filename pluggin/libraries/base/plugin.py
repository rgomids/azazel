import gi

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
import wave

from consts import AZAZEL_STONE
from gi.repository import AppIndicator3, Gtk



class Plugin:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            "Azazel",
            f"{AZAZEL_STONE.FOLDER}/7V7.gif",
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS,
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.make_sidebar()

    def make_sidebar(self):

        menu = Gtk.Menu()

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
            menu.append(radio_item)

        # Item de exemplo no menu
        separator = Gtk.SeparatorMenuItem()
        menu.append(separator)

        # Botão de gravar/parar
        self.is_recording = False

        record_item = Gtk.MenuItem.new()
        record_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.record_icon = Gtk.Image.new_from_icon_name(
            "microphone-sensitivity-high", Gtk.IconSize.MENU
        )
        self.record_label = Gtk.Label(label="Start Recording")
        record_box.pack_start(self.record_icon, False, False, 0)
        record_box.pack_start(self.record_label, False, False, 5)
        record_item.add(record_box)
        record_item.connect("activate", self.on_record_toggle)
        menu.append(record_item)

        # Item de exemplo no menu
        separator = Gtk.SeparatorMenuItem()
        menu.append(separator)

        # Item de sair
        quit_item = Gtk.MenuItem.new_with_label("Quit")
        quit_item.connect("activate", self.on_quit)
        menu.append(quit_item)

        menu.show_all()

        self.indicator.set_menu(menu)

        self.start()

    def on_quit(self):
        Gtk.main_quit()
        # TODO: parar tbmm o servidor go e fechar o programa
        

    def start(self):
        Gtk.main()
