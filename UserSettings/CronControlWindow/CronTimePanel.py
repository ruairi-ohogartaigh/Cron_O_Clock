# cron time selector control panel

import gi
import datetime
gi.require_version('Adw', '1')
gi.require_version('Gtk', '4.0')

from gi.repository import Adw, Gio, GObject, Gtk


class ControlPanel(Gtk.Box):
    def __init__(self):
        super().__init__()#title="Cron Control Panel")

        grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        self.append(grid)

        # Time selector
        time_label = Gtk.Label(label="Time of day (HH:MM):")
        # Hour selector
        self.hour_spin = Gtk.SpinButton()
        self.hour_spin.connect("value-changed", self.on_hour_spin_selected)
        self.hour_spin.set_range(0, 23)
        self.hour_spin.set_value(datetime.datetime.now().hour)
        self.hour_spin.set_increments(1, 1)
        
        # minute selector
        self.minute_spin = Gtk.SpinButton()
        self.minute_spin.connect("value-changed", self.on_minute_spin_selected)
        self.minute_spin.set_range(0, 59)
        self.minute_spin.set_value(datetime.datetime.now().minute)
        self.minute_spin.set_increments(1, 1)

        # Quick day selector
        quick_day = Gtk.Label(label="Quick Select:")
        quick_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.quick_day_toggles = []
        quick_names = ["Week-days", "Weekend", "Everyday"]
        for typ in quick_names:
            btn = Gtk.ToggleButton(label=typ)
            if typ == "Week-days":
                btn.connect("toggled", self.on_weekdays_toggled)
            elif typ == "Weekend":
                btn.connect("toggled", self.on_weekend_toggled)
            elif typ == "Everyday":
                btn.connect("toggled", self.on_everyday_toggled)
            btn.connect("toggled", lambda b: print(f"Quick selection: {b.get_label()}"))
            quick_box.append(btn)
            self.quick_day_toggles.append(btn)

        # Days of week selector (toggle buttons)
        day_label = Gtk.Label(label="Days of Week:")
        days_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.day_toggles = []
        day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in day_names:
            btn = Gtk.ToggleButton(label=day)
            btn.connect("toggled", lambda b: print(f"Selected day: {b.get_label()}"))
            days_box.append(btn)
            self.day_toggles.append(btn)

        # Months selector (toggle buttons in a FlowBox for multi-select)
        month_label = Gtk.Label(label="Months/Seasons:")
        months_box = Gtk.ComboBoxText()
        month_names = ["All","Winter","Jan", "Feb","Spring","Mar", "Apr", "May","Summer","Jun", 
                   "Jul", "Aug","Autumn", "Sep", "Oct", "Nov", "Dec"]
        for month in month_names:
            months_box.append_text(month)
        months_box.set_active(0)
        self.month_combo = months_box

        PanelTitle = Gtk.Label(label=" Configure Cron Job time and frequency: ")
        PanelTitle.set_halign(Gtk.Align.CENTER)
        PanelTitle.set_markup('<span size="large" weight="bold"> Configure Cron Job time and frequency: </span>')

        grid.attach(PanelTitle, 0, 0, 1, 1)
        # hours and minutes selectors
        grid.attach(time_label, 0, 1, 1, 1)
        grid.attach(self.hour_spin, 1, 1, 1, 1)
        grid.attach(self.minute_spin, 2, 1, 1, 1)
        
        # day and month selectors
        grid.attach(quick_day, 0, 2, 1, 1)
        grid.attach(quick_box, 1, 2, 2, 1)
        grid.attach(day_label, 0, 3, 1, 1)
        grid.attach(days_box, 1, 3, 2, 1)
        grid.attach(month_label, 0, 4, 1, 1)
        grid.attach(months_box, 1, 4, 2, 1)

        # Feedback to user
        feedback_label = Gtk.Label(label="Current Configuration:")
        # Use Gtk.Entry widgets for feedback so they can be updated easily
        time_fb = Gtk.Label()
        time_fb.set_text("cron will be called at: "+str(self.get_selected_time()))
        #time_fb.set_editable(False)
        days_fb = Gtk.Label()
        days_fb.set_text(" on these days: "+str(self.get_selected_days()))
        #days_fb.set_editable(False)
        months_fb = Gtk.Entry()
        months_fb.set_text(" These Months: "+str(self.get_selected_months()))
        #months_fb.set_editable(False)
        months_fb = Gtk.Label(label=str(self.get_selected_months()))


        # Store feedback labels for later updates
        self.time_fb = time_fb
        self.days_fb = days_fb
        self.months_fb = months_fb

        # Connect signals to update feedback labels
        self.hour_spin.connect("value-changed", lambda w: self.update_feedback())
        self.minute_spin.connect("value-changed", lambda w: self.update_feedback())
        for btn in self.day_toggles:
            btn.connect("toggled", lambda b: self.update_feedback())
        self.month_combo.connect("changed", lambda w: self.update_feedback())

        # Initial feedback update
        self.update_feedback()
        grid.attach(feedback_label, 0, 5, 1, 1)
        grid.attach(time_fb, 1, 5, 1, 1)
        grid.attach(days_fb, 2, 5, 1, 1)
        grid.attach(months_fb, 3, 5, 1, 1)



    def get_selected_time(self):
            hour = int(self.hour_spin.get_value())
            minute = int(self.minute_spin.get_value())
            return f"{hour:02}:{minute:02}"

    def get_selected_days(self):
            selected_days = []
            for btn in self.day_toggles:
                if btn.get_active():
                    selected_days.append(btn.get_label())
            return selected_days

    def get_selected_months(self):
            selected_months = []
            active_month = self.month_combo.get_active_text()
            if active_month:
                selected_months.append(active_month)
            return selected_months

    def get_quick_day_selection(self):
            for btn in self.quick_day_toggles:
                if btn.get_active():
                    return btn.get_label()
            return None


    ## Action handlers methods
    ##ui feedback methods
    def update_feedback(self):
        self.time_fb.set_text("cron will be called at: "+self.get_selected_time())
        self.days_fb.set_text(" these days: "+str(self.get_selected_days()))
        self.months_fb.set_text(" during "+str(self.get_selected_months()))

    ## action handlers for time buttons
    def on_hour_spin_selected(self, spin_button):
        
        hour = int(spin_button.get_value())
        if hour < 0 or hour > 23:
            spin_button.set_value(0)  # Reset to 0 if out of range
        else:
            print(f"Selected hour: {hour:02}")
            self.setHr = hour

    def on_minute_spin_selected(self, spin_button):
        minute = int(spin_button.get_value())
        if minute < 0 or minute > 59:
            spin_button.set_value(0)  # Reset to 0 if out of range
        else:
            print(f"Selected minute: {minute:02}")
            self.setMin = minute


    # Quick select days 
    def on_weekdays_toggled(self, button):
        if button.get_active():
            for btn in self.day_toggles:
                if btn.get_label() in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
                    btn.set_active(True)
        else:
            for btn in self.day_toggles:
                if btn.get_label() in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
                    btn.set_active(False)
                    print("Weekdays toggled off "+ btn.get_label())
    def on_weekend_toggled(self, button):
        if button.get_active():
            for btn in self.day_toggles:
                if btn.get_label() in ["Sat", "Sun"]:
                    btn.set_active(True)
        else:
            for btn in self.day_toggles:
                if btn.get_label() in ["Sat", "Sun"]:
                    btn.set_active(False)

    def on_everyday_toggled(self, button):
        if button.get_active():
            for btn in self.day_toggles:
                btn.set_active(True)
        else:
            for btn in self.day_toggles:
                btn.set_active(False)



# if __name__ == "__main__":
#     app = Gtk.Application()
#     def on_activate(app):
#         win = Gtk.ApplicationWindow(application=app)
#         win.set_default_size(600, 400)
#         panel = ControlPanel()
#         win.set_child(panel)
#         win.present()
#     app.connect("activate", on_activate)
#     app.run()