import gi
from gi.repository import GdkPixbuf

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import cell


class MainWindow(Gtk.Window):
    flowbox = Gtk.FlowBox()

    def __init__(self):
        super().__init__(title="imágenes")
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(400, 400)

        header = Gtk.HeaderBar(title="Mis cosas favoritas")
        header.set_subtitle("SIUUU")
        header.props.show_close_button = True

        self.set_titlebar(header)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER,Gtk.PolicyType.AUTOMATIC)
        scrolled.add(self.flowbox)
        self.add(scrolled)
        image1 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/MonadoREX+.jpg", 200, 200, False)
        image1.set_from_pixbuf(pixbuf)
        image2 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/bolaSmash.jpg", 200, 200, False)
        image2.set_from_pixbuf(pixbuf)
        image3 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/cello.jpg", 200, 200, False)
        image3.set_from_pixbuf(pixbuf)
        image4 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/oureol.jpg", 200, 200, False)
        image4.set_from_pixbuf(pixbuf)
        image5 = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/empanadah.jpg", 200, 200, False)
        image5.set_from_pixbuf(pixbuf)
        cell_one = cell.Cell("Monado REX+", image1)
        cell_two = cell.Cell("Bola Smash", image2)
        cell_three = cell.Cell("Cello",image3)
        cell_four = cell.Cell("Oreo", image4)
        cell_five = cell.Cell("Empanadah", image5)
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
