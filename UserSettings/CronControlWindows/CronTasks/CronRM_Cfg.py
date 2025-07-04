## This command window will be used to allow users to remove tasks from the cron

# this class will contain the widget used to configure the
# alarm  image, message and display times
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import  Gtk
import os
import shutil

from CronController import CronIO
# here we will use the CronIO to check crontab for value remove the task from the crontab

class CronRmCfg(Gtk.Box):

    ## for functionality of this class, we want feedback from cron_io to confirm the users input is present in the crontab
    # this will require some kind of grep command to check if the task_cmd is present in the crontab
    # otherwise  we need to give feedback that the task_cmd is not present


    def __init__(self, parent, cron_io, task_cmd): # task_cmd is the command to be removed
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.parent = parent
        # Image path entry
        img_label = Gtk.Label(label="Command to be removed:")
        img_label.set_halign(Gtk.Align.START)
        self.img_entry = Gtk.Entry()
        add_img_button = Gtk.Button(label="Remove")



        # Add widgets to the box
        self.append(img_label)
        Img_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        Img_box.append(self.img_entry)
        self.img_entry.connect("changed", self.on_command_selected)
        # Img_box.append(add_img_button)



        self.append(Img_box)


    def on_command_selected(self, combo):
        # Get the selected command
        selected_command = combo.get_active_text()
        if selected_command:
            self.img_entry.set_text(selected_command)
            # Here we would call the CronIO to remove the task from the crontab
            # cron_io.remove_task(selected_command)
            print(f"Command to be removed: {selected_command}")
        else:
            print("No command selected")