__author__ = 'dandro'

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class TimeRowForm(Widget):
	def __init__(self,  **kwargs):
		super(TimeRowForm, self).__init__(**kwargs)
		self.text_project = ObjectProperty()
		self.text_description = ObjectProperty()
		self.build_ui()

	def build_ui(self):
		self.text_project = TextInput(hint_text='Project Name', multiline=False, background_normal='fake',
			background_active='fake')
		self.add_widget(self.text_project)

		self.text_description = TextInput(hint_text='Task Description', multiline=True, background_normal='fake',
			background_active='fake')
		self.add_widget(self.text_description)
