#This UI will be a srolling window that will display the context existing in crontab

import gi
import io
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject

class CronLog(Gtk.Box):

    def __init__(self, parent):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self.parent = parent

        # Title label for the log
        title_label = Gtk.Label(label=" Crontab Schedule:", xalign=0)
        title_label.set_margin_bottom(6)
        title_label.set_css_classes([" Content of Crontab:"])
        title_label.set_markup('<span size="large" weight="bold"> Content of Crontab: </span>')
        self.append(title_label)

        # Scrolled window for log
        self.scrolled = Gtk.ScrolledWindow()
        self.scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.scrolled.set_min_content_height(200)
        self.scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled.set_hexpand(True)
        self.scrolled.set_vexpand(True)
        self.append(self.scrolled)

        # Container for log lines
        self.log_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.scrolled.set_child(self.log_box)

        # Dummy info for mocking crontab -l
        self.cron_log = Gio.File.new_for_path("Cron_O_Clock/UserSettings/CronControlWindows/cron_demo.txt")
        self.load_log(self.cron_log)
    
    def load_log(self, gio_file):
        try:
            stream = gio_file.read(None)
            data = stream.read_bytes(4096, None)
            text = data.get_data().decode("utf-8")
            for line in text.splitlines():
                label = Gtk.Label(label=line, xalign=0)
                label.set_css_classes(["cron-log-line"])
                self.log_box.append(label)
        except Exception as e:
            label = Gtk.Label(label=f"Error loading log: {e}", xalign=0)
            label.set_css_classes(["cron-log-line"])
            self.log_box.append(label)

        # Apply CSS for background and text color
        css = b"""
        .cron-log-line {
            color: #00FF00;
            background: transparent;
        }
        .cron-log-bg {
            background: #000000;
        }
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css)
        Gtk.StyleContext.add_provider_for_display(
            self.get_display(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        self.log_box.set_css_classes(["cron-log-bg"])
        self.scrolled.set_css_classes(["cron-log-bg"])

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