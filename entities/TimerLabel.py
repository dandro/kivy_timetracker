__author__ = 'dandro'

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
import time


class TimerLabel(Widget):
	def __init__(self, parent_size, **kwargs):
		super(TimerLabel, self).__init__(**kwargs)

		# schedule clock
		Clock.schedule_interval(self.update_time, 1)

		# init attributes
		self.parent_size = parent_size
		self.size = (self.parent_size[0], 50)
		self.pos = (0, self.parent_size[1] - self.height)

		# Create and Add time_label
		self.time_label = Label(text=self.display_time(), pos=self.pos, size=self.size, font_size=24, markup=True)
		self.add_widget(self.time_label)

		# Set UI
		with self.time_label.canvas:
			Color(0, 0, 0, 0.12)
			Rectangle(size=self.size, pos=self.pos)

	@staticmethod
	def display_time():
		return "[b]" + time.asctime() + "[/b]"

	def update_time(self, dt):
		self.time_label.text = self.display_time()