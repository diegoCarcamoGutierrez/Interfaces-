import gi
from gi.repository import Gtk
class SimpleMenu(Gtk.Window):
    def __init__(self):
        super().__init__(title="Acerca del desarrollador")
        label = Gtk.Label("Diego Cárcamo es un estudiante de 2º de DAM")
        self.add(label)
