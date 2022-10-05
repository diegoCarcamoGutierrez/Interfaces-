import gi
from gi.repository.Gtk import Button

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class NoWindow(Gtk.Window):
    button = Gtk.Button(label="No")

    def __init__(self):
        super().__init__(title="noWindow")
#       self.connect("destroy", Gtk.main_quit)
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("no")
