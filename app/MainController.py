from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.logger import Logger
from app.TimerLabel import TimerLabel
from app.TimeRowForm import TimeRowForm
from app.TimeParser import TimeParser
from app.StackRowLabel import StackRowLabel
from pickledb import pickledb
from datetime import date, timedelta, datetime
import os.path

ROWS_IN_STACK = 7


class MainController(Widget):
    def __init__(self, window_size, **kwargs):
        super(MainController, self).__init__(**kwargs)
        self.name = "Main Controller"
        self.timer_label = TimerLabel(parent_size=window_size)
        self.current_day = date.today()
        self.current_day_display = Label(text=self.update_current_day_display(), markup=True)
        self.db = self.get_db_file()
        self.stack_current_limit = 0

        self.stack_src = []
        self.submit_button = Button()
        self.button_previous_day = Button()
        self.button_next_day = Button()
        self.button_up = Button()
        self.button_down = Button()
        self.row_form = TimeRowForm()
        self.button_report = Button()
        self.stack_layout = StackLayout()

        self.on_load()

    def get_db_file(self, today=date.today()):
        # Create today file if it doesn't exists
        self.current_day = today
        self.current_day_display.text = self.update_current_day_display()
        db_filename = "./db/" + str(self.current_day) + "_timelog.db"
        if not os.path.isfile(db_filename):
            timelog_file = open(db_filename, 'a')
            timelog_file.write("{}")
            timelog_file.close()

        return pickledb(db_filename, False)

    def update_current_day_display(self):
        return '[color=b2b2b2]' + str(self.current_day.strftime('%a %d %b %Y')) + '[/color]'

    def on_load(self):
        self.build_stack_src(self.db).bind_buttons().update_stack_view(len(self.stack_src))

    def build_stack_src(self, db):
        # sort db rows by key/timestamp
        row_set = set(db.getall())
        row_list = list(row_set)
        row_list.sort()
        for key in row_list:
            self.stack_src.append(db.get(key))
        return self

    def bind_buttons(self):
        self.submit_button.bind(on_press=self.add_new_row)
        self.button_previous_day.bind(on_press=self.load_previous_day)
        self.button_next_day.bind(on_press=self.load_next_day)
        self.button_up.bind(on_press=self.go_up)
        self.button_down.bind(on_press=self.go_down)
        self.button_report.bind(on_press=self.run_report)
        return self

    def load_previous_day(self, button):
        self.db = self.get_db_file(self.previous_day(self.current_day))
        self.clear_stack_src().build_stack_src(self.db).update_stack_view(len(self.stack_src))

    def load_next_day(self, button):
        if not self.current_day == date.today():
            self.db = self.get_db_file(self.next_day(self.current_day))
            self.clear_stack_src().build_stack_src(self.db).update_stack_view(len(self.stack_src))

    @staticmethod
    def previous_day(current_day=date.today()):
        return current_day - timedelta(days=1)

    @staticmethod
    def next_day(current_day=date.today()):
        return current_day + timedelta(days=1)

    def go_up(self, button):
        limit = self.stack_current_limit - 1 if self.stack_current_limit > ROWS_IN_STACK else self.stack_current_limit
        self.update_stack_view(limit)

    def go_down(self, button):
        limit = min(self.stack_current_limit + 1, len(self.stack_src))
        self.update_stack_view(limit)

    def run_report(self, button):
        TimeParser(self.db).parse_rows()

    def update_stack_src(self, project_title, project_description):
        row = self.build_row_dict(self.timer_label.time_label.text, self.timer_label.time_label.time, project_title,
            project_description)
        self.stack_src.append(row)
        return self

    def clear_stack_src(self):
        self.stack_src = []
        return self

    def insert_row(self, row):
        self.db.set(str(datetime.now()), row)
        self.db.dump()
        return self

    @staticmethod
    def build_row_dict(time_text, time, project_title, project_description):
        return {
            'time_text': time_text,
            'time': time,
            'project_title': project_title,
            'project_description': project_description
        }

    def add_new_row(self, button):
        project_title = self.row_form.text_project.text
        project_description = self.row_form.text_description.text
        self.insert_row(self.build_row_dict(self.timer_label.time_label.text, self.timer_label.time_label.time,
            project_title, project_description))
        self.update_stack_src(project_title, project_description)
        self.update_stack_view(len(self.stack_src))
        self.row_form.text_description.text = ''

    def get_style_stack_row(self, row):
        stack_row = self.display_row_label(self.stack_src[row])
        stack_row.size = 300, 30
        stack_row.pos_hint = {'right': 1, 'center_y': 0.5}
        return stack_row

    def update_stack_view(self, limit):
        self.stack_current_limit = limit
        stack_range = self.get_stack_range(limit)
        self.stack_layout.clear_widgets()
        for row in range(stack_range['start'], stack_range['limit']):
            stack_row = self.get_style_stack_row(row)
            self.stack_layout.add_widget(stack_row)

        return self

    @staticmethod
    def get_stack_range(limit):
        start = 0 if limit - ROWS_IN_STACK <= 0 else limit - ROWS_IN_STACK
        return {'start': start, 'limit': limit}

    @staticmethod
    def display_row_label(row_dict):
        return Label(text=row_dict['time_text'] + " - \n" + row_dict['project_title'] + " "
                          + row_dict['project_description'], size_hint=(1., .1), pos=(0, 0), markup=True)

    # return StackRowLabel(row_dict['time_text'], row_dict['project_title'] + row_dict['project_description'])

    @staticmethod
    def rgba2float(r, g, b, a=1.0):
        return float("{0:.2f}".format(r / 256.0)), float("{0:.2f}".format(g / 256.0)), float(
            "{0:.2f}".format(b / 256.0)), a

    @staticmethod
    def log_str(value):
        Logger.info(str(value))
