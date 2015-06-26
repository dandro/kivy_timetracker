__author__ = 'dmartinez'

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

import time


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)


class TimeTrackerApp(App):
	def __init__(self, **kwargs):
		super(TimeTrackerApp, self).__init__(**kwargs)
		self.timer = Timer()
		self.root_widget = BoxLayout(orientation='horizontal', size=(WINDOW_WIDTH, WINDOW_HEIGHT))

	def build(self):
		print"started"
		self.timer.start()
		self.root_widget.add_widget(self.timer.display_time)
		return self.root_widget


class Timer(Widget):
	def __init__(self, **kwargs):
		super(Timer, self).__init__(**kwargs)
		self.current_time = time.clock()
		self.display_time = Label(text=str(self.current_time), font_size=20)

	def start(self):
		Clock.schedule_interval(self.update_time, 1)

	def update_time(self, dt):
		self.current_time = time.clock()
		self.display_time.text = str(self.current_time)
		print"my time: {}, var {}".format(self.current_time, dt)


if __name__ == '__main__':
	TimeTrackerApp().run()