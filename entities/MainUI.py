__author__ = 'dandro'

from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image

from entities.TimerLabel import TimerLabel
from entities.TimeRowForm import TimeRowForm

WINDOW_SIZE = 400, 768


class MainUI(Widget):
	def __init__(self, **kwargs):
		super(MainUI, self).__init__(**kwargs)
		self.register_event_type('on_row_added')

		# Set MainUI Attributes
		self.size = WINDOW_SIZE

		# UI Background
		self.add_widget(Image(source='./assets/PyStalkerBackground.png', size=WINDOW_SIZE))

		# Add Timer Label
		self.timer_label = TimerLabel(parent_size=WINDOW_SIZE)
		self.add_widget(self.timer_label)

		# Add Time Row Form
		self.row_form = TimeRowForm(self.timer_label.relative_top)
		self.add_widget(self.row_form)

		# Set UI Stack Layout
		self.layout_stack = StackLayout(orientation='tb-lr', size=(WINDOW_SIZE[0], 413),
			padding=10, spacing=5)
		self.add_widget(self.layout_stack)

	def on_row_added(self, text_project, text_description):
		self.layout_stack.add_widget(Label(text=self.timer_label.time_label.text + " - \n" + text_project + " "
		+ text_description, size_hint=(1., .1), markup=True))

	@staticmethod
	def rgba2float(r, g, b, a=1.0):
		return float("{0:.2f}".format(r/256.0)), float("{0:.2f}".format(g/256.0)), float("{0:.2f}".format(b/256.0)), a
