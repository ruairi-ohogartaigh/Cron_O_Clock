# this class will contain help information for the user
from gi.repository import Adw, Gtk, GObject
import os
import shutil


class HelpCfg(Gtk.Box):


    def __init__(self, user=None):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)

        # Image path entry
        img_label = Gtk.Label(label=" App documentation: to be appended")
        img_label.set_halign(Gtk.Align.START)

        # Add widgets to the box
        self.append(img_label)


