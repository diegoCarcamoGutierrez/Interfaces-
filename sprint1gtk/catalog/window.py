import gi

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

        cell_one = cell.Cell("Monado REX+", Gtk.Image.new_from_file("data/edited/MonadoREX+.jpg"))
        cell_two = cell.Cell("Bola Smash", Gtk.Image.new_from_file("data/edited/bolaSmash.jpg"))
        cell_three = cell.Cell("Cello", Gtk.Image.new_from_file("data/edited/cello.jpg"))
        cell_four = cell.Cell("Oreo", Gtk.Image.new_from_file("data/edited/oureol.jpg"))
        cell_five = cell.Cell("Empanadah", Gtk.Image.new_from_file("data/edited/empanadah.jpg"))
        self.flowbox.add(cell_one)
        self.flowbox.add(cell_two)
        self.flowbox.add(cell_three)
        self.flowbox.add(cell_four)
        self.flowbox.add(cell_five)
