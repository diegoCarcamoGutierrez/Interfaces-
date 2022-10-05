import gi
from gi.repository.Gtk import Button

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class YesWindow(Gtk.Window):
    button = Gtk.Button(label="Yes")

    def __init__(self):
        super().__init__(title="yesWindow")
#       self.connect("destroyer", Gtk.main_quit)
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("yes")