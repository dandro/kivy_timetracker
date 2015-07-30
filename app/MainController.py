__author__ = 'dmartinez'

from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.logger import Logger
from app.TimerLabel import TimerLabel
from app.TimeRowForm import TimeRowForm
from app.TimeParser import TimeParser
from pickledb import pickledb
import time
from datetime import date, timedelta
import os.path

ROWS_IN_STACK = 6


class MainController(Widget):
	def __init__(self, window_size, **kwargs):
		super(MainController, self).__init__(**kwargs)
		self.name = "Main Controller"
		self.register_event_type('on_row_added')
		self.timer_label = TimerLabel(parent_size=window_size)
		self.current_day = date.today()
		self.db = self.get_db_file()
		self.stack_current_limit = 0

		self.stack_src = []
		self.button_previous_day = Button()
		self.button_next_day = Button()
		self.button_up = Button()
		self.button_down = Button()
		self.row_form = TimeRowForm(start_top=self.timer_label.relative_top, window_size=window_size, controller=self)
		self.button_report = Button()
		self.stack_layout = StackLayout()

		self.on_load()

	def get_db_file(self, today=date.today()):
		# Create today file if it doesn't exists
		self.current_day = today
		db_filename = "./db/" + str(self.current_day) + "_timelog.db"
		if not os.path.isfile(db_filename):
			timelog_file = open(db_filename, 'a')
			timelog_file.write("{}")
			timelog_file.close()

		return pickledb(db_filename, False)

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
		row = self.build_row_dict(self.timer_label.time_label.text, self.timer_label.time_label.time, project_title, project_description)
		self.stack_src.append(row)
		return self

	def clear_stack_src(self):
		self.stack_src = []
		return self

	def insert_row(self, row):
		self.db.set(str(time.time()), row)
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

	def on_row_added(self, project_title, project_description):
		self.insert_row(self.build_row_dict(self.timer_label.time_label.text, self.timer_label.time_label.time,
			project_title, project_description))
		self.update_stack_src(project_title, project_description)
		self.update_stack_view(len(self.stack_src))

	def update_stack_view(self, limit):
		self.stack_current_limit = limit
		stack_range = self.get_stack_range(limit)
		self.stack_layout.clear_widgets()
		for row in range(stack_range['start'], stack_range['limit']):
			self.stack_layout.add_widget(self.display_row_label(self.stack_src[row]))

		return self

	@staticmethod
	def get_stack_range(limit):
		start = 0 if limit - ROWS_IN_STACK <= 0 else limit - ROWS_IN_STACK
		return {'start': start, 'limit': limit}

	@staticmethod
	def display_row_label(row_dict):
		return Label(text=row_dict['time_text'] + " - \n" + row_dict['project_title'] + " "
		+ row_dict['project_description'], size_hint=(1., .1), markup=True)

	@staticmethod
	def rgba2float(r, g, b, a=1.0):
		return float("{0:.2f}".format(r/256.0)), float("{0:.2f}".format(g/256.0)), float("{0:.2f}".format(b/256.0)), a

	@staticmethod
	def log_str(value):
		Logger.info(str(value))
