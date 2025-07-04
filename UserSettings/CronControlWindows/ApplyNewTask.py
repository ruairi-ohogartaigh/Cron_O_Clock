## panel that will summarise user selection before appending changes to cron

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from CronControlWindows import CronTimePanel
from CronControlWindows.CronTasks import CronCmdCfg, CronAlrmCfg, CronRM_Cfg, HelpCfg


class ApplyNewTask(Gtk.Box):
    
    def __init__(self, parent, cron_time_panel, cron_tasks_panel):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.parent = parent
        self.cron_time_panel = cron_time_panel
        # Label for confirmation
        self.confirm_label = Gtk.Label(label="Confirm your task settings:")
        self.confirm_label.set_halign(Gtk.Align.START)
        grid = Gtk.Grid(column_spacing=10, row_spacing=10)


        # Button to apply changes
        self.apply_button = Gtk.Button(label="Apply Changes")
        self.apply_button.connect("clicked", self.on_apply_clicked)


        feedback_label = Gtk.Label(label="Current Configuration:")
        self.append(feedback_label)


        self.CronTimePanel = CronTimePanel.CronTimePanel(self)


        feedback_label = Gtk.Label(label="Current Configuration:")
        # Use Gtk.Entry widgets for feedback so they can be updated easily
        self.time_fb = Gtk.Label()
        self.time_fb.set_text("cron will be called at: "+str(self.CronTimePanel.get_selected_time()))
        self.days_fb = Gtk.Label()
        self.days_fb.set_text(" on these days: "+str(self.CronTimePanel.get_selected_days()))
        self.months_fb = Gtk.Entry()
        self.months_fb.set_text(" These Months: "+str(self.CronTimePanel.get_selected_months()))
        self.months_fb = Gtk.Label(label=str(self.CronTimePanel.get_selected_months()))




        #added
        grid.attach(self.confirm_label, 0, 2, 1, 1)
        grid.attach(self.apply_button, 0, 6, 1, 1)
        #grid.attach(self.apply_button, 0, 1, 1, 1)

        grid.attach(self.time_fb, 0, 3, 1, 1)
        grid.attach(self.days_fb, 1, 3, 1, 1)
        grid.attach(self.months_fb, 2, 3, 1, 1)
        grid.set_hexpand(True)
        grid.set_vexpand(True)
        self.append(grid)


        # for btn in self.day_toggles:
        #     btn.connect("toggled", lambda b: self.CronTimePanel.update_feedback())
        #     self.update_feedback()



    def on_apply_clicked(self, button):
        # Here you would implement the logic to apply the new task settings
        # For now, we will just print a message
        print("Applying new task settings...")
        self.update_feedback()  # Update feedback in ApplyNewTask panel
        # You can also update the UI or notify the user as needed
        self.confirm_label.set_text("Task settings applied successfully!")
        self.apply_button.set_sensitive(False)



    def update_feedback(self):
        self.time_fb.set_text("cron will be called at: " + self.cron_time_panel.get_selected_time())
        self.days_fb.set_text(" these days: " + str(self.cron_time_panel.get_selected_days()))
        self.months_fb.set_text(" during " + str(self.cron_time_panel.get_selected_months()))


