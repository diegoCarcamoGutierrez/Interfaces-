import gi
from gi.repository import Gtk
import gtk


class SimpleMenu(Gtk.Window):
    def __init__(self, lab):
        super().__init__(title="Acerca del desarrollador")
        label = Gtk.Label(lab)
        self.add(label)
