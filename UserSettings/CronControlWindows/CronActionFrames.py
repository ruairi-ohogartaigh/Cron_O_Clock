import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


#from CronControlWindows 
from CronControlWindows import CronTimePanel
from CronControlWindows import ApplyNewTask
from CronControlWindows import CronTaskPanel #import CronIO
from CronControlWindows import CronLog
from CronController import CronIO


class Cron_Action_Frames(Gtk.Box):
    def __init__(self, parent):
        super().__init__()

        # self.CronTimePanel = CronTimePanel(self)
        # self.CronTaskPanel = CronTaskPanel(self)
        # self.ApplyNewTask = ApplyNewTask(self)
        grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        self.CronTimePanel = CronTimePanel.CronTimePanel(self)
        self.CronTaskPanel = CronTaskPanel.CronTaskPanel(self)
        self.ApplyNewTask = ApplyNewTask.ApplyNewTask(self, self.CronTimePanel, self.CronTaskPanel)
        self.CronIO = CronIO.CronIO(self.ApplyNewTask)
        self.CronLog = CronLog.CronLog(self,self.CronIO)
        grid.attach(self.CronTimePanel,0,1,1,1)
        grid.attach(self.CronTaskPanel, 0, 2, 1, 1)
        grid.attach(self.ApplyNewTask ,0,3,1,1)
        grid.attach(self.CronLog, 0, 4, 1, 1)
        # self.CronTimePanel.grid(row=1, column=1)
        # self.CronTaskPanel.grid(row=2, column=1)
        # self.ApplyNewTask.grid(row=3, column=1)

        self.append(grid)




def update_feedback(self):
    self.time_fb.set_text("cron will be called at: "+self.get_selected_time())
    self.days_fb.set_text(" these days: "+str(self.get_selected_days()))
    self.months_fb.set_text(" during "+str(self.get_selected_months()))
    if self.apply_new_task is not None:
        self.apply_new_task.update_feedback()