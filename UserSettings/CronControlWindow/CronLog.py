#This UI will be a srolling window that will display the context existing in crontab

import gi
import io
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject

class CronLog(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_hexpand(True)
        self.set_vexpand(True)

        # Scrolled window for log
        self.scrolled = Gtk.ScrolledWindow()
        self.scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.scrolled.set_hexpand(True)
        self.scrolled.set_vexpand(True)
        self.append(self.scrolled)

        # Container for log lines
        self.log_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.scrolled.set_child(self.log_box)

        # Dummy info for mocking
        self.cron_log = Gio.File.new_for_path("cron_demo.txt")

# scroll needs to be fixed for this gui

# if __name__ == "__main__":
#     app = Gtk.Application()

#     def on_activate(app):
#         win = Gtk.ApplicationWindow(application=app)
#         win.set_default_size(500, 300)
#         log_widget = CronLog()
#         win.set_child(log_widget)
#         #win.log_box.get_first().set_child(log_widget)
#         win.present()

#     app.connect("activate", on_activate)
#     app.run()