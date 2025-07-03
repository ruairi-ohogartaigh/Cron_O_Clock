## panel that will summarise user selection before appending changes to cron

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from CronControlWindows import CronTimePanel


class ApplyNewTask(Gtk.Box):
    
    def __init__(self, parent):
        super().__init__(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_start(12)
        self.set_margin_end(12)
        self.parent = parent
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
        time_fb = Gtk.Label()
        time_fb.set_text("cron will be called at: "+str(self.CronTimePanel.get_selected_time()))
        #time_fb.set_editable(False)
        days_fb = Gtk.Label()
        days_fb.set_text(" on these days: "+str(self.CronTimePanel.get_selected_days()))
        #days_fb.set_editable(False)
        months_fb = Gtk.Entry()
        months_fb.set_text(" These Months: "+str(self.CronTimePanel.get_selected_months()))
        #months_fb.set_editable(False)
        months_fb = Gtk.Label(label=str(self.CronTimePanel.get_selected_months()))


        # Store feedback labels for later updates
        # self.CronTimePanel.time_fb = self.parent.CronTimePanel.time_fb
        # self.CronTimePanel.days_fb = self.parent.CronTimePanel.days_fb
        # self.CronTimePanel.months_fb = self.parent.CronTimePanel.months_fb



        #PanelTitle.set_markup('<span size="large" weight="bold"> New Task summary: </span>')
        #PanelTitle.set_halign(Gtk.Align.START)
        #self.append(PanelTitle)
        self.append(self.confirm_label)
        self.append(self.apply_button)
        self.append(time_fb)
        #self.update_feedback()
        self.append(feedback_label)
        self.append(time_fb)
        self.append(days_fb)
        self.append(months_fb)

        # for btn in self.day_toggles:
        #     btn.connect("toggled", lambda b: self.CronTimePanel.update_feedback())
        #     self.update_feedback()



    def on_apply_clicked(self, button):
        # Here you would implement the logic to apply the new task settings
        # For now, we will just print a message
        print("Applying new task settings...")
        # You can also update the UI or notify the user as needed
        self.confirm_label.set_text("Task settings applied successfully!")
        self.apply_button.set_sensitive(False)

    def update_feedback(self):
        self.time_fb.set_text("cron will be called at: "+self.parent.CronTimePanel.get_selected_time())
        self.days_fb.set_text(" these days: "+str(self.parent.CronTimePanel.get_selected_days()))
        self.months_fb.set_text(" during "+str(self.parent.CronTimePanel.get_selected_months()))

