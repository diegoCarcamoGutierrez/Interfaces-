import gi
import yes_window
import no_window

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    button = Gtk.Button(label="Yes")
    res = Gtk.Label("inicio")
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

    def __init__(self):
        super().__init__(title="Main")
        self.connect("destroy", Gtk.main_quit)
        self.label1 = Gtk.Label("Inicio")
        self.add(self.box)
        self.box.pack_start(self.res, True, True, 0)
        self.box.pack_start(self.box1, True, True, 0)

        self.button1 = Gtk.Button(label="Yes")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box1.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="No")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box1.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        win = yes_window.YesWindow()
        win.show_all()

    def on_button2_clicked(self, widget):
        win = no_window.NoWindow()
        win.show_all()

