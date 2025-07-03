import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


#from CronControlWindows 
from CronControlWindows import CronTimePanel
from CronControlWindows import ApplyNewTask
from CronControlWindows import CronTaskPanel #import CronIO
from CronControlWindows import CronLog



class Cron_Action_Frames(Gtk.Box):
    def __init__(self, parent):
        super().__init__()

        # self.CronTimePanel = CronTimePanel(self)
        # self.CronTaskPanel = CronTaskPanel(self)
        # self.ApplyNewTask = ApplyNewTask(self)
        grid = Gtk.Grid(column_spacing=10, row_spacing=10)

        self.ApplyNewTask = ApplyNewTask.ApplyNewTask(self)
        self.CronTimePanel = CronTimePanel.CronTimePanel(self)
        self.CronTaskPanel = CronTaskPanel.CronTaskPanel(self)
        self.CronLog = CronLog.CronLog(self)
        grid.attach(self.CronTimePanel,0,1,1,1)
        grid.attach(self.CronTaskPanel, 0, 2, 1, 1)
        grid.attach(self.ApplyNewTask ,0,3,1,1)
        grid.attach(self.CronLog, 0, 4, 1, 1)
        # self.CronTimePanel.grid(row=1, column=1)
        # self.CronTaskPanel.grid(row=2, column=1)
        # self.ApplyNewTask.grid(row=3, column=1)

        self.append(grid)



## test class
# if __name__ == "__main__":
#     app = Gtk.Application()

#     def on_activate(app):
#         win = Gtk.ApplicationWindow(application=app)
#         win.set_title("Cron Scheduler")
#         win.set_default_size(800, 600)

#         action_frames = Cron_Action_Frames(win)

#         vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
#         vbox.append(action_frames)

#         win.set_child(vbox)
#         win.present()

#     app.connect("activate", on_activate)
#     app.run()

def update_feedback(self):
    self.time_fb.set_text("cron will be called at: "+self.get_selected_time())
    self.days_fb.set_text(" these days: "+str(self.get_selected_days()))
    self.months_fb.set_text(" during "+str(self.get_selected_months()))
    if self.apply_new_task is not None:
        self.apply_new_task.update_feedback()