# This Class will configure the GUI for task setup
   

from gi.repository import Gtk, GObject

from CronControlWindow import  CronCmdCfg, CronAlrmCfg ,HelpCfg

class CronTaskPanel(Gtk.Box):


    def __init__(self, user=None):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_hexpand(True)
        self.set_vexpand(True)

        PanelTitle = Gtk.Label(label=" Configure Cron Task:")
        PanelTitle.set_markup('<span size="large" weight="bold"> Configure Cron Tasks: </span>')
    
        CmdCfg = CronCmdCfg.CronCmdCfg()
        cfg = CronAlrmCfg.CronAlrmCfg()
        HlpCfg = HelpCfg.HelpCfg()
            # Create a notebook for alarm and command config

        notebook = Gtk.Notebook()
        notebook.set_tab_pos(Gtk.PositionType.TOP)
        notebook.set_show_tabs(True)
        notebook.set_show_border(True)
        #notebook.set_property("tab-label", Gtk.Label(label="Cron Command:"))
        notebook.append_page(cfg, Gtk.Label(label="Add pop-up notification"))
        notebook.append_page(CmdCfg, Gtk.Label(label="Add command line task"))
        notebook.append_page(HlpCfg, Gtk.Label(label="help"))

        self.append(PanelTitle)
        self.append(notebook)