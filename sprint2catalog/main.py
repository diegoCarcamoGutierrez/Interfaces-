import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import window
from load_window import LoadWindow

# Mostrar la ventana principal
win = LoadWindow()
win.show_all()

Gtk.main()
