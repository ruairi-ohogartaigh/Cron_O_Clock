import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
import os
import shutil


class CronAlrmCfg(Gtk.Box):


    def __init__(self, parent, cron_cmd=None):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.parent = parent


        # Store feedback labels for later updates
        set_img="No image set"
        set_min=0
        set_sec=0
        set_msg="No message set"
        set_T_in_secs=0 

        self.set_img=set_img
        self.set_min=set_min
        self.set_sec=set_sec
        self.set_T_in_secs=set_T_in_secs
        self.set_msg=set_msg

        # Image path entry
        img_label = Gtk.Label(label="Image Path:")
        img_label.set_halign(Gtk.Align.START)
        self.img_entry = Gtk.ComboBoxText()
        dirname = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','..', 'AlarmWindow/ImgLib'))
        img_dir = dirname
        if os.path.isdir(img_dir):
            for fname in sorted(os.listdir(img_dir)):
                fpath = os.path.join(img_dir, fname)
                if os.path.isfile(fpath):
                    self.img_entry.append_text(fname)
        self.img_entry.set_hexpand(True)
        self.img_entry.connect("changed", self.on_img_selected)
        # button to append image to directory
        add_img_button = Gtk.Button(label="+")
        add_img_button.set_halign(Gtk.Align.END)


        # Time frame selector
        time_label = Gtk.Label(label="Set Notification visibility for(MM:SS):")
        time_label.set_halign(Gtk.Align.START)
        self.min_spin = Gtk.SpinButton()
        self.min_spin.set_range(0, 59)
        self.min_spin.set_value(0)
        self.min_spin.set_increments(1, 1)
        self.sec_spin = Gtk.SpinButton()
        self.sec_spin.set_range(0, 59)
        self.sec_spin.set_value(0)
        self.sec_spin.set_increments(1, 1)
        # Connect value-changed signals to on_apply_clicked
        self.min_spin.connect("minute value-changed", self.on_min_selected)
        self.sec_spin.connect("second value-changed", self.on_sec_selected)


        # Message entry
        msg_label = Gtk.Label(label="Notification Message:")
        msg_label.set_halign(Gtk.Align.START)
        self.msg_entry = Gtk.Entry()
        self.msg_entry.set_placeholder_text("Enter message")
        self.msg_entry.set_hexpand(True)
        self.msg_entry.connect("message changed", self.on_msg_selected)

        # Add widgets to the box
        self.append(img_label)
        Img_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        Img_box.append(self.img_entry)
        Img_box.append(add_img_button)

        self.append(Img_box)
        self.append(time_label)
        # Create a horizontal box to hold the spin buttons side by side
        time_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        time_box.append(self.min_spin)
        time_box.append(self.sec_spin)
        self.append(time_box)
        self.append(msg_label)
        self.append(self.msg_entry)
        self.cmdline_args = Gtk.Label()
        update_feedback_text = self.update_feedback_text()

    def on_img_selected(self, combo_box):
        self.set_img = combo_box.get_active_text()
        update_feedback_text = self.update_feedback_text()

    def on_min_selected(self, spin_button):
        min_value = int(spin_button.get_value())
        if min_value < 0 or min_value > 59:
            spin_button.set_value(0)
        self.set_min= min_value
        update_feedback_text = self.update_feedback_text()

    def on_sec_selected(self, spin_button):
        sec_value = int(spin_button.get_value())
        if sec_value < 0 or sec_value > 59:
            spin_button.set_value(0)
        self.set_sec = sec_value
        update_feedback_text = self.update_feedback_text()

    def on_msg_selected(self, entry):
        msg_value = entry.get_text()
        if not msg_value:
            entry.set_text("No message set")
        self.set_msg = msg_value
        update_feedback_text = self.update_feedback_text()


    def update_feedback(self):
        return f'--image "{self.get_selected_img_name()}" --message "{self.get_selected_msg()}" --displaytime {self.get_selected_timeframe()}'


    def get_selected_img_name(self):
        return self.set_img
    
    def get_selected_msg(self):
        return self.set_msg
    
    def get_selected_timeframe(self):
        # Convert minutes to seconds
        int_min_val = (int(self.set_min))*60  
        sec_val = int(self.set_sec)  # Seconds remain as is
        timeframe_in_seconds = int_min_val + sec_val
        return str(timeframe_in_seconds)
    
    def update_feedback_text(self):
        self.cmdline_args.set_text("Current Configuration: "+self.update_feedback())
        self.append(self.cmdline_args)
