# This Class will configure the GUI for task setup
   

from gi.repository import Gtk

from CronControlWindows.CronTasks import CronCmdCfg, CronAlrmCfg, CronRM_Cfg ,HelpCfg
from CronController import CronIO
from CronControlWindows import ApplyNewTask


class CronTaskPanel(Gtk.Box):


    def __init__(self, parent, cron_io=None):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_hexpand(True)
        self.set_vexpand(True)
        self.parent = parent
        self.cron_io = cron_io
        PanelTitle = Gtk.Label(label=" Configure Cron Task:")
        PanelTitle.set_markup('<span size="large" weight="bold"> Configure Cron Tasks: </span>')
        PanelTitle.set_halign(Gtk.Align.START)


        #as there are multiple panels where the task can be configured, we need this parameter
        # this will keep track of which the user has selected
        self.task_cmd=["src", "cmd"]


        self.CronCmdCfg = CronCmdCfg.CronCmdCfg(self, self.cron_io, self.task_cmd)
        self.CronAlrmCfg = CronAlrmCfg.CronAlrmCfg(self, self.cron_io, self.task_cmd)
        self.CronRM_Cfg = CronRM_Cfg.CronRmCfg(self ,self.cron_io, self.task_cmd)
        self.HelpCfg = HelpCfg.HelpCfg(self)
            # Create a notebook for alarm and command config

        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.PositionType.TOP)
        self.notebook.set_show_tabs(True)
        self.notebook.set_show_border(True)
        #notebook.set_property("tab-label", Gtk.Label(label="Cron Command:"))
        self.notebook.append_page(self.CronAlrmCfg, Gtk.Label(label="Add pop-up notification"))
        self.notebook.append_page(self.CronCmdCfg, Gtk.Label(label="Add command line task"))
        self.notebook.append_page(self.CronRM_Cfg, Gtk.Label(label="Remove task"))
        self.notebook.append_page(self.HelpCfg, Gtk.Label(label="help"))
        self.notebook.connect("switch-page", self.on_page_changed)
        self.append(PanelTitle)
        self.append(self.notebook)



    def on_page_changed(self, notebook, page, page_num):
        """Called when the user switches notebook tabs"""
        self.get_selected_task()
        # Notify parent to update feedback
        if hasattr(self.parent, 'update_feedback'):
            self.parent.update_feedback()
    
    def update_feedback(self):
        """Called by child task configuration panels to notify parent"""
        self.get_selected_task()
        # Forward the update to our parent (ApplyNewTask)
        if hasattr(self.parent, "ApplyNewTask"):
            self.parent.ApplyNewTask.update_feedback()
    
    def get_selected_task(self):
        format="Task selected: "
        current_page_index = self.notebook.get_current_page()
        print(f"DEBUG: Current page index: {current_page_index}")
        if current_page_index == 0: 
            self.task_cmd[0]="notification"
            self.task_cmd[1]=self.CronAlrmCfg.update_feedback()
            print(f"DEBUG: Notification task: {self.task_cmd[1]}")

        elif current_page_index == 1:
            self.task_cmd[0]="command"
            self.task_cmd[1]=self.CronCmdCfg.update_feedback()
            print(f"DEBUG: Command task: {self.task_cmd[1]}")

        elif current_page_index == 2:
            self.task_cmd[0]="remove"
            self.task_cmd[1]=self.CronRM_Cfg.update_feedback()
            print(f"DEBUG: Remove task: {self.task_cmd[1]}")

        else:
            self.task_cmd[0]="none"
            self.task_cmd[1]="No cronjob selected"
        return f" Task type: {self.task_cmd[0]} with command: {self.task_cmd[1]}"
        
    def update_task_cmd(self):
        print(f"DEBUG: update_task_cmd called, current task_cmd[0]: {self.task_cmd[0]}")
        if self.task_cmd[0]=="notification":
            self.task_cmd[1]=self.CronAlrmCfg.update_feedback()
        elif self.task_cmd[0]=="command":
            self.task_cmd[1]=self.CronCmdCfg.update_feedback()
        elif self.task_cmd[0]=="remove":
            self.task_cmd[1]=self.CronRM_Cfg.update_feedback()
        else:
            self.task_cmd[1]="none"
        print(f"DEBUG: update_task_cmd returning: {self.task_cmd[1]}")
        return self.task_cmd[1]

    def get_task_cmd(self):
        """Returns the current task command configuration"""
        return self.task_cmd