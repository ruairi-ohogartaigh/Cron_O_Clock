import gi
import os
import argparse
import sys
gi.require_version("Gtk", "3.0")
gi.require_version('Pango', '1.0')
from gi.repository import Pango, Gtk, Gdk, GLib

# Parse arguments
parser = argparse.ArgumentParser(description="Show an alarm window with image and message.")
parser.add_argument('--image', '-i', required=True, help='Path to background image')
parser.add_argument('--message', '-m', required=True, help='Message to display')
parser.add_argument('--displaytime', '-t', type=int, default=10, help='Seconds to display the window')
args = parser.parse_args()

script_dir = os.path.dirname(__file__)
image_path = script_dir+'/ImgLib/'+args.image
message = args.message
display_time = args.displaytime

if not os.path.exists(image_path):
    print(f"Image not found: {image_path}")
    sys.exit(1)

win = Gtk.Window()
win.set_title("Alarm")
win.set_default_size(600, 400)

overlay = Gtk.Overlay()
image = Gtk.Image.new_from_file(image_path)
overlay.add(image)

label = Gtk.Label(label=message)
pangoFont = Pango.FontDescription("Sans 24")
label.modify_font(pangoFont)
label.set_name("alarm-label")
label.set_halign(Gtk.Align.CENTER)
label.set_valign(Gtk.Align.CENTER)
overlay.add_overlay(label)

# Add CSS for label color and background
css = b"""
#alarm-label {
    background: rgba(255,255,255,0.7);
    color: black;
    padding: 20px;
    border-radius: 10px;
}
"""
style_provider = Gtk.CssProvider()
style_provider.load_from_data(css)
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(),
    style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

win.add(overlay)
win.connect("destroy", Gtk.main_quit)
win.show_all()

# Auto-close after display_time seconds
GLib.timeout_add_seconds(display_time, win.close)

Gtk.main()