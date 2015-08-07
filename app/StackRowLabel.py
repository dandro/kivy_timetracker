__author__ = 'dandro'

from kivy.uix.widget import Widget
from kivy.uix.label import Label


class StackRowLabel(Widget):
	def __init__(self, time_text, project_text, **kwargs):
		super(StackRowLabel, self).__init__(**kwargs)
		self.time_label = Label(text=time_text, markup=True)
		self.project_label = Label(text=project_text)
		self.size = 300, 40
		self.build_ui()

	def build_ui(self):
		self.add_widget(self.time_label)
		self.add_widget(self.project_label)