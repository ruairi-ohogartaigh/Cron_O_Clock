## panel that will summarise user selection before appending changes to cron
from gi.repository import Gtk, GObject

class ApplyNewTask(Gtk.Box):
    def __init__(self, user=None):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)

        # Label for confirmation
        self.confirm_label = Gtk.Label(label="Confirm your task settings:")
        self.confirm_label.set_halign(Gtk.Align.START)

        # Button to apply changes
        self.apply_button = Gtk.Button(label="Apply Changes")
        self.apply_button.connect("clicked", self.on_apply_clicked)

        # Add widgets to the box
        self.append(self.confirm_label)
        self.append(self.apply_button)

    def on_apply_clicked(self, button):
        # Here you would implement the logic to apply the new task settings
        # For now, we will just print a message
        print("Applying new task settings...")
        # You can also update the UI or notify the user as needed
        self.confirm_label.set_text("Task settings applied successfully!")
        self.apply_button.set_sensitive(False)