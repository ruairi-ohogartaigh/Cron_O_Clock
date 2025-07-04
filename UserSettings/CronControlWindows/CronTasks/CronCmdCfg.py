# this class will contain the widget used to configure the
# alarm  image, message and display times
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import  Gtk
import os
import shutil


class CronCmdCfg(Gtk.Box):


    def __init__(self, parent, task_cmd):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.parent = parent
        # Image path entry
        img_label = Gtk.Label(label="User defined command line argument:")
        img_label.set_halign(Gtk.Align.START)
        self.img_entry = Gtk.Entry()
        add_img_button = Gtk.Button(label="Test Command")



        # Add widgets to the box
        self.append(img_label)
        Img_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        Img_box.append(self.img_entry)
        # Img_box.append(add_img_button)

        self.append(Img_box)


# local debugging code
# if __name__ == "__main__":
#     app = Gtk.Application()
#     def on_activate(app):
#         win = Gtk.ApplicationWindow(application=app)
#         cfg = CronCmdCfg()
#         win.set_child(cfg)
#         win.present()
#     app.connect("activate", on_activate)
#     app.run()