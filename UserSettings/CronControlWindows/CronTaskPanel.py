# This Class will configure the GUI for task setup
   

from gi.repository import Gtk

from CronControlWindows.CronTasks import CronCmdCfg, CronAlrmCfg, CronRM_Cfg ,HelpCfg
from CronController import CronIO

class CronTaskPanel(Gtk.Box):


    def __init__(self, parent, cron_io=None):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self.parent = parent
        PanelTitle = Gtk.Label(label=" Configure Cron Task:")
        PanelTitle.set_markup('<span size="large" weight="bold"> Configure Cron Tasks: </span>')
        PanelTitle.set_halign(Gtk.Align.START)


        #as there are multiple panels where the task can be configured, we need this parameter
        # this will keep track of which the user has selected
        task_cmd=""


        self.CronCmdCfg = CronCmdCfg.CronCmdCfg(self, task_cmd)
        self.CronAlrmCfg = CronAlrmCfg.CronAlrmCfg(self, task_cmd)
        self.CronRM_Cfg = CronRM_Cfg.CronRmCfg(self ,cron_io, task_cmd)
        self.HelpCfg = HelpCfg.HelpCfg(self)
            # Create a notebook for alarm and command config

        notebook = Gtk.Notebook()
        notebook.set_tab_pos(Gtk.PositionType.TOP)
        notebook.set_show_tabs(True)
        notebook.set_show_border(True)
        #notebook.set_property("tab-label", Gtk.Label(label="Cron Command:"))
        notebook.append_page(self.CronAlrmCfg, Gtk.Label(label="Add pop-up notification"))
        notebook.append_page(self.CronCmdCfg, Gtk.Label(label="Add command line task"))
        notebook.append_page(self.CronRM_Cfg, Gtk.Label(label="Remove task"))
        notebook.append_page(self.HelpCfg, Gtk.Label(label="help"))

        self.append(PanelTitle)
        self.append(notebook)

    def get_task_value(self):
        return self.get_selected_task().get_active_text()