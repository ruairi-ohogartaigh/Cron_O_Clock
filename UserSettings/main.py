# This is the main script for user settings gui
# it will initialise the gui and backend with the CronController

import gi

#from Cron_O_Clock.UserSettings.CronControlWindow import CronAlrmCfg
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Adw


from CronControlWindow import CronLog,  CronTimePanel,  ApplyNewTask, CronTaskPanel




if __name__ == "__main__":
    app = Gtk.Application()
    def on_activate(app):
        win = Gtk.ApplicationWindow(application=app)
        win.set_title("Cron Scheduler")
        ctrlP = CronTimePanel.ControlPanel()
        log = CronLog.CronLog()
        AddTask = ApplyNewTask.ApplyNewTask()
        TskCfg=CronTaskPanel.CronTaskPanel()



        # Create a vertical box to hold all panels
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.append(ctrlP)          # cron time config
        vbox.append(TskCfg)        # cron task configuration
        vbox.append(AddTask)        # add/remove from crontab
        vbox.append(log)           # cron log viewer    


        win.set_child(vbox)
        win.present()
    app.connect("activate", on_activate)
    app.run()

