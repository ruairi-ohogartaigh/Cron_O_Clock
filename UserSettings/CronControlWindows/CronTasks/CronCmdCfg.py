# this class will contain the widget used to configure the
# alarm  image, message and display times
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import  Gtk
import os
import shutil


class CronCmdCfg(Gtk.Box):


    def __init__(self, parent, cron_io, task_cmd):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.parent = parent
        self.cmd = ["cmd", ""]
        # Image path entry
        cmd_label = Gtk.Label(label="User defined command line argument:")
        cmd_label.set_halign(Gtk.Align.START)
        self.cmd_entry = Gtk.Entry()
        self.cmd_entry.connect("changed", self.on_command_selected)


        # Add widgets to the box
        self.append(cmd_label)
        cmd_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        cmd_box.append(self.cmd_entry)
        self.append(cmd_box)


        # debug feedback
        self.msg_entry = Gtk.Label()
        self.msg_entry.set_hexpand(True)
        self.msg_entry.set_text("enter command")
        #self.msg_entry.connect("changed", self.on_msg_selected)

        self.append(self.msg_entry)
        self.cmdline_args = Gtk.Label()
        update_feedback_text = self.update_feedback()


    def on_command_selected(self, entry):
        # Get the selected command
        self.cmd[0] = "cmd"
        self.cmd[1] = entry.get_text()
        self.msg_entry.set_text("command: " + self.update_feedback_txt())
        if self.cmd[1]:
            print(f"Command to be executed: {self.cmd[1]}")
            # Notify parent to update feedback
            if hasattr(self.parent, 'update_feedback'):
                self.parent.update_feedback()
        else:
            print("No command selected")

    def get_command(self):
        return self.cmd
    

    def update_feedback_txt(self):
        return self.cmd_entry.get_text()


    def update_feedback(self):
        self.cmd[0] = "cmd"
        self.cmd[1] = self.cmd_entry.get_text()
        return f'command:  "{self.get_command()[1]}" will be executed by cron'

    def on_msg_selected(self, entry):
        msg_value = entry.get_text()
        if not msg_value:
            entry.set_text("No message set")
        self.set_msg = msg_value
        update_feedback_text = self.update_feedback_text()
        # Notify parent to update feedback
        if hasattr(self.parent, 'update_feedback'):
            self.parent.update_feedback()
