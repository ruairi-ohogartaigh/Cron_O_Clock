import gi
import datetime
gi.require_version('Adw', '1')
gi.require_version('Gtk', '4.0')

from gi.repository import Adw, Gio, GObject, Gtk


class ControlPanel(Gtk.GObject, Gtk.ListBox):
    def __init__(self):
        super().__init__(title="Cron Control Panel")
        self.set_resizable(True)
        self.set_default_size(400, 220)

        grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        self.set_child(grid)

        # Time selector
        time_label = Gtk.Label(label="Time (HH:MM):")
        self.hour_spin = Gtk.SpinButton()
        self.hour_spin.set_range(0, 23)
        self.hour_spin.set_value(datetime.datetime.now().hour)
        self.hour_spin.set_increments(1, 1)
        self.minute_spin = Gtk.SpinButton()
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
            quick_box.append(btn)
            self.quick_day_toggles.append(btn)

        # Days of week selector (toggle buttons)
        day_label = Gtk.Label(label="Days of Week:")
        days_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.day_toggles = []
        day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in day_names:
            btn = Gtk.ToggleButton(label=day)
            days_box.append(btn)
            self.day_toggles.append(btn)

        # Months selector (toggle buttons in a FlowBox for multi-select)
        month_label = Gtk.Label(label="Months:")
        months_box = Gtk.FlowBox()
        months_box.set_max_children_per_line(6)
        months_box.set_selection_mode(Gtk.SelectionMode.NONE)
        self.month_toggles = []
        month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                       "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for month in month_names:
            btn = Gtk.ToggleButton(label=month)
            months_box.append(btn)
            self.month_toggles.append(btn)

        # Year selector
        year_label = Gtk.Label(label="Year:")
        self.year_spin = Gtk.SpinButton()
        thisYr= datetime.date.today().year
        self.year_spin.set_range(thisYr, thisYr+100)
        self.year_spin.set_value(thisYr)
        self.year_spin.set_increments(1, 1)

        # Add widgets to grid
        grid.attach(time_label, 0, 0, 1, 1)
        grid.attach(self.hour_spin, 1, 0, 1, 1)
        grid.attach(self.minute_spin, 2, 0, 1, 1)
        grid.attach(quick_day, 0, 1, 1, 1)
        grid.attach(quick_box, 1, 1, 2, 1)
        grid.attach(day_label, 0, 2, 1, 1)
        grid.attach(days_box, 1, 2, 2, 1)
        grid.attach(month_label, 0, 3, 1, 1)
        grid.attach(months_box, 1, 3, 2, 1)
        grid.attach(year_label, 0, 4, 1, 1)
        grid.attach(self.year_spin, 1, 4, 2, 1)

# if __name__ == "__main__":
#     app = Gtk.Application()
#     def on_activate(app):
#         win = ControlPanel()
#         win.set_application(app)
#         win.present()
#     app.connect("activate", on_activate)
#     app.run()