#Mostrar ventana de detalles del objeto enviado
import gi
from gi.repository import GdkPixbuf
import window
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class DetailWindow(Gtk.Window):

    def __init__(self,tit,desc,imagen):
        super().__init__(title="Ventana detallada")
        box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=4)
        box.pack_start(Gtk.Label(label=tit),False,False,0)
        box.pack_start(Gtk.Label(label=desc),False,False,0)
        box.pack_start(imagen,True,True,0)
        self.add(box)



