# this class will contain the widget used to configure the
# alarm  image, message and display times
from gi.repository import Adw, Gtk, GObject
import os
import shutil


class CronCmdCfg(Gtk.Box):


    def __init__(self, user=None):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)

        # Image path entry
        img_label = Gtk.Label(label="Image Path:")
        img_label.set_halign(Gtk.Align.START)
        self.img_entry = Gtk.ComboBoxText()
        dirname = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'AlarmWindow/ImgLib'))
        img_dir = dirname
        if os.path.isdir(img_dir):
            for fname in sorted(os.listdir(img_dir)):
                fpath = os.path.join(img_dir, fname)
                if os.path.isfile(fpath):
                    self.img_entry.append_text(fname)
        self.img_entry.set_hexpand(True)

        # button to append image to directory
        add_img_button = Gtk.Button(label="+")
        add_img_button.set_halign(Gtk.Align.END)

        def on_add_img_clicked(button):
            dialog = Gtk.FileChooserDialog(
                title="Select Image",
                parent=self.get_root(),
                action=Gtk.FileChooserAction.OPEN,
                buttons=(
                    "Cancel", Gtk.ResponseType.CANCEL,
                    "Open", Gtk.ResponseType.ACCEPT
                )
            )
            dialog.set_modal(True)
            dialog.set_select_multiple(False)
            dialog.set_current_folder(os.path.expanduser("~"))
            filter_img = Gtk.FileFilter()
            filter_img.set_name("Image files")
            filter_img.add_mime_type("image/png")
            filter_img.add_mime_type("image/jpeg")
            filter_img.add_mime_type("image/gif")
            filter_img.add_pattern("*.png")
            filter_img.add_pattern("*.jpg")
            filter_img.add_pattern("*.jpeg")
            filter_img.add_pattern("*.gif")
            dialog.add_filter(filter_img)

            response = dialog.run()
            if response == Gtk.ResponseType.ACCEPT:
                src_path = dialog.get_file().get_path()
            fname = os.path.basename(src_path)
            dest_path = os.path.join(dirname, fname)
            if not os.path.exists(dest_path):
                shutil.copy(src_path, dest_path)
                self.img_entry.append_text(fname)
            dialog.destroy()

        add_img_button.connect("clicked", on_add_img_clicked)



        # Time frame selector
        time_label = Gtk.Label(label="Alert is visible for(MM:SS):")
        self.min_spin = Gtk.SpinButton()
        self.min_spin.set_range(0, 59)
        self.min_spin.set_value(0)
        self.min_spin.set_increments(1, 1)
        self.sec_spin = Gtk.SpinButton()
        self.sec_spin.set_range(0, 59)
        self.sec_spin.set_value(0)
        self.sec_spin.set_increments(1, 1)


        # Message entry
        msg_label = Gtk.Label(label="Message:")
        msg_label.set_halign(Gtk.Align.START)
        self.msg_entry = Gtk.Entry()
        self.msg_entry.set_placeholder_text("Enter message")
        self.msg_entry.set_hexpand(True)

        # Add widgets to the box
        self.append(img_label)
        Img_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        Img_box.append(self.img_entry)
        Img_box.append(add_img_button)

        self.append(Img_box)
        self.append(time_label)
        # Create a horizontal box to hold the spin buttons side by side
        time_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        time_box.append(self.sec_spin)
        time_box.append(self.min_spin)
        self.append(time_box)
        self.append(msg_label)
        self.append(self.msg_entry)

## local debugging code
# if __name__ == "__main__":
#     app = Gtk.Application()
#     def on_activate(app):
#         win = Gtk.ApplicationWindow(application=app)
#         cfg = CronCmdCfg()
#         win.set_child(cfg)
#         win.present()
#     app.connect("activate", on_activate)
#     app.run()