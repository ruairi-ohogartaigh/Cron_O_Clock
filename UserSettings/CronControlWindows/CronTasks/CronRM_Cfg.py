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
        self.cron_io = cron_io
        self.cmd = ["remove", ""]

        # Image path entry
        rm_label = Gtk.Label(label="Command to be removed:")
        rm_label.set_halign(Gtk.Align.START)
        self.rm_entry= Gtk.Entry()
        self.rm_entry.connect("changed", self.on_command_selected)


        self.feedback_label = Gtk.Label()
        self.feedback_label.set_text("enter command to be removed")


        # Add widgets to the box
        self.append(rm_label)
        rm_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        rm_box.append(self.rm_entry)
        self.rm_entry.connect("changed", self.on_command_selected)
        # rm_box.append(add_rm_button)

        self.append(rm_box)
        self.append(self.feedback_label)



    def on_command_selected(self, entry):

        self.feedback_label.set_text("Remove command: "+self.rm_entry.get_text())
        self.update_feedback()

        if hasattr(self.parent, 'update_feedback'):
            self.parent.update_feedback()


    def update_feedback(self):
        self.cmd = ["remove", self.rm_entry.get_text()] 
        return f'remove command:  "{self.rm_entry.get_text()}" from the crontab'
