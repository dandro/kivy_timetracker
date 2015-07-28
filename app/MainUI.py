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

		# Add load day before button
		self.controller.button_previous_day.size = 130, 30
		self.controller.button_previous_day.text = 'Load Prev Day'
		self.controller.button_previous_day.top = WINDOW_SIZE[1] - 10
		self.controller.button_previous_day.right = 140
		self.add_widget(self.controller.button_previous_day)

		# Add load day before button
		self.controller.button_next_day.size = 130, 30
		self.controller.button_next_day.text = 'Load Next Day'
		self.controller.button_next_day.top = WINDOW_SIZE[1] - 10
		self.controller.button_next_day.right = WINDOW_SIZE[0] - 10
		self.add_widget(self.controller.button_next_day)

		# Add button up
		self.controller.button_up.size = WINDOW_SIZE[0] - 20, 30
		self.controller.button_up.text = 'Up'
		self.controller.button_up.top = 402
		self.controller.button_up.right = WINDOW_SIZE[0] - 10
		self.add_widget(self.controller.button_up)

		# Add Button down
		self.controller.button_down.size = WINDOW_SIZE[0] - 20, 30
		self.controller.button_down.text = 'Down'
		self.controller.button_down.top = 100
		self.controller.button_down.right = WINDOW_SIZE[0] - 10
		self.add_widget(self.controller.button_down)

		# Add Time Row Form
		self.add_widget(self.controller.row_form)

		# Add Button down
		self.controller.button_report.size = 130, 30
		self.controller.button_report.text = 'report'
		self.controller.button_report.pos = 10, self.controller.row_form.submit_button_top
		self.add_widget(self.controller.button_report)

		# Set UI Stack Layout
		self.controller.stack_layout.orientation = 'tb-lr'
		self.controller.stack_layout.size = (WINDOW_SIZE[0], 360)
		self.controller.stack_layout.padding = 10
		self.controller.stack_layout.spacing = 5
		self.add_widget(self.controller.stack_layout)
