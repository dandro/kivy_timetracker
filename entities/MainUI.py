__author__ = 'dandro'

from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image

from entities.TimerLabel import TimerLabel

WINDOW_SIZE = 400, 768


class MainUI(Widget):
	def __init__(self, **kwargs):
		super(MainUI, self).__init__(**kwargs)

		# Set MainUI Attributes
		self.orientation = 'vertical'
		self.size = WINDOW_SIZE
		background = self.rgba2int(222, 229, 105, 0.78)
		with self.canvas:
			Color(background[0], background[1], background[2], background[3])
			Rectangle(size=self.size, pos=self.pos)

		# UI Background
		self.add_widget(Image(source='./assets/PyStalkerBackground.png', size=WINDOW_SIZE))

		# Timer Label
		self.timer_label = TimerLabel(parent_size=WINDOW_SIZE)
		self.add_widget(self.timer_label)

		# Set UI Stack Layout
		self.layout_stack = StackLayout(orientation='tb-lr', size=(WINDOW_SIZE[0], self.timer_label.relative_top),
			padding=10, spacing=5)
		self.layout_stack.add_widget(Button(text="Add Time", size_hint=(1., .1)))
		self.layout_stack.add_widget(Button(text="Add Time", size_hint=(1., .1)))
		self.layout_stack.add_widget(Button(text="Add Time", size_hint=(1., .1)))
		self.add_widget(self.layout_stack)


	@staticmethod
	def rgba2int(r, g, b, a=1.0):
		return float("{0:.2f}".format(r/256.0)), float("{0:.2f}".format(g/256.0)), float("{0:.2f}".format(b/256.0)), a
