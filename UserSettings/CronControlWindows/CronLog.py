#This UI will be a srolling window that will display the context existing in crontab

import gi
import io
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio, GObject
from CronController import CronIO

class CronLog(Gtk.Box):

    def __init__(self, parent, cron_io=None):
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
        self.cron_io = cron_io
        cron_io.get_cron_jobs()
        cron_jobs = self.cron_io.get_cron_jobs()
        self.load_log_from_string(cron_jobs)


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


    def load_log_from_string(self, text):
        try:
            for line in text:
                label = Gtk.Label(label="\n"+line, xalign=0)
                label.set_css_classes(["cron-log-line"])
                self.log_box.append(label)
        except Exception as e:
            label = Gtk.Label(label=f"Error loading log: {e}", xalign=0)
            label.set_css_classes(["cron-log-line"])
            self.log_box.append(label)
