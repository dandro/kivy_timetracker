__author__ = 'dandro'

from kivy.uix.widget import Widget
from kivy.uix.image import Image
from app.MainController import MainController

WINDOW_SIZE = 400, 768


class MainUI(Widget):
	def __init__(self, **kwargs):
		super(MainUI, self).__init__(**kwargs)
		self.controller = MainController(window_size=WINDOW_SIZE)
		self.build_ui()

	def build_ui(self):
		# Set MainUI Attributes
		self.size = WINDOW_SIZE

		# UI Background
		self.add_widget(Image(source='./assets/PyStalkerBackground.png', size=WINDOW_SIZE))

		# Add Timer Label
		self.add_widget(self.controller.timer_label)

		# Add Time Row Form
		self.add_widget(self.controller.row_form)

		# Set UI Stack Layout
		self.add_widget(self.controller.stack_layout)
