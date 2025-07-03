# This is the main script for user settings gui
# it will initialise the gui and backend with the CronController

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GObject
import datetime
import sys_state

#from CronControlWindows import CronLog,  CronActionFrames
from CronControlWindows import CronTimePanel, ApplyNewTask, CronTaskPanel, CronLog
from CronControlWindows import CronActionFrames
#CronActionFrames
from CronController import CronIO




if __name__ == "__main__":
    app = Gtk.Application()
    def on_activate(app):
        win = Gtk.ApplicationWindow(application=app)
        win.set_title("Cron Scheduler")
        win.set_default_size(800, 600)

        #log = CronLog.CronLog()
        action_frames = CronActionFrames.Cron_Action_Frames(win)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.append(action_frames)
        #vbox.append(log)

        win.set_child(vbox)
        win.present()
    app.connect("activate", on_activate)
    app.run()

