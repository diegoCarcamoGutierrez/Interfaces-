import gi
import simple_menu

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self, data_source):
        super().__init__(title="imágenes")
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        #Definición de la pestaña "Help", que se mostrará arriba a la izquierda de la ventana principal
        mb = Gtk.MenuBar()

        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("Help")
        filem.set_submenu(filemenu)

        h = Gtk.MenuItem("About developer")
        h.connect("activate", show_simple_window) #conexión con el método que enseñará la nueva ventana con la información del desarrolador
        filemenu.append(h)

        mb.append(filem)

        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)

        header = Gtk.HeaderBar(title="Mis cosas favoritas")
        header.set_subtitle("Asc")
        header.props.show_close_button = True
        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        vbox.add(scrolled)
        self.add(vbox)

        # mostrar en la ventana principal las imágenes
        for item in data_source:
            cell = Cell(item.get("name"), item.get("gtk_image"))
            self.flowbox.add(cell)

def show_simple_window(self):  #Mostrar la ventana con la información del desarrollador (texto libre)
    hwin = simple_menu.SimpleMenu()
    hwin.show_all()
