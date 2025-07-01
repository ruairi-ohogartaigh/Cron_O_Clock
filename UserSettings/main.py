# This is the main script for user settings gui
# it will initialise the gui and backend with the CronController

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Adw

from CronControlWindow import ControlPanel, CronCmdCfg, CronLog

def main():
    # This function is the entry point for the application
    # It will create the application and run it
    pass
    


if __name__ == "__main__":

    ControlPanel = ControlPanel()
    CronCmdCfg = CronCmdCfg()
    CronLog = CronLog()
    

    # Run the application
    app.run(None)