import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from window import MainWindow
from no_window import NoWindow
from yes_window import YesWindow
win = MainWindow()
win.show_all()

Gtk.main()
