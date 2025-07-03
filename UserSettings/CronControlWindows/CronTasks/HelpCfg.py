# this class will contain help information for the user
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import  Gtk
import os
import shutil


class HelpCfg(Gtk.Box):


    def __init__(self, parent):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.parent = parent
        # Image path entry
        img_label = Gtk.Label(label=" App documentation: to be appended from .txt or .md file")
        img_label.set_halign(Gtk.Align.START)

        # Add widgets to the box
        self.append(img_label)


