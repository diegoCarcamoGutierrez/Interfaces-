from email.mime import image

from gi.repository import GdkPixbuf
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import detail_window


class Cell(Gtk.EventBox):
    name = None

    def __init__(self, name, image):
        super().__init__()
        self.name = name
        self.image = image
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click, self.image, self.name)

    def on_click(self, widget, event, imagen, name):
        # El programa abrirá una nueva ventana detallada
        image = Gtk.Image()
        image.set_from_pixbuf(imagen.get_pixbuf())

        #Carga de una imagen, un título y una descripción según la celda que se clique
        if self.name == "Monado REX+":
            tit = "Monado REX+"
            descript = "Esta espada fue diseñada por el mecánico Shulk luego de desaparecer la Monado original"
        elif self.name == "Bola Smash":
            tit = "Bola Smash"
            descript = "Bola que otorga poder inmenso a aquella persona que consiga romperla"
        elif self.name == "Cello":
            tit = "Cello"
            descript = "Instrumento musical propio de la musica de cámara. Resalta por su tamaño y estilo, además de su característico sonido"
        elif self.name == "Oreo":
            tit = "Oreo"
            descript = "Galletas conocidas por todo el mundo. Tan ricas como dañinas para el estómago"
        elif self.name == "Empanadah":
            tit = "Empanada"
            descript = "Dicen que si te venden una empanada en Argentina, podria llevar carne NO animal..."

        #Carga de la nueva ventana detallada, pasándole el título, la descripción y la imagen de la celda clicada como parámetro
        nwin = detail_window.DetailWindow(tit, descript, image)
        nwin.show_all()
