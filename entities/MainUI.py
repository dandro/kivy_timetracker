__author__ = 'dandro'

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Rectangle
from kivy.config import Config

from entities.TimerLabel import TimerLabel

WINDOW_SIZE = 400, 768


class MainUI(BoxLayout):
	def __init__(self, **kwargs):
		super(MainUI, self).__init__(**kwargs)

		# Set MainUI Attributes
		self.orientation = 'vertical'
		self.size = WINDOW_SIZE
		background = self.rgba2int(222, 229, 105, 0.78)
		with self.canvas:
			Color(background[0], background[1], background[2], background[3])
			Rectangle(size=self.size, pos=self.pos)

		# Set up outer layout
		# layout_outer = BoxLayout(orientation='vertical', size=(self.width, 30))
		# layout_outer.add_widget(TimerLabel(parent_size=layout_outer.size))
		# self.add_widget(layout_outer)

		# Set UI Stack Layout
		# layout_stack = StackLayout(orientation='tb-lr', size=WINDOW_SIZE, pos=(0, 0))
		# layout_stack.add_widget()
		self.add_widget(TimerLabel(parent_size=WINDOW_SIZE))

	@staticmethod
	def rgba2int(r, g, b, a=1.0):
		return float("{0:.2f}".format(r/256.0)), float("{0:.2f}".format(g/256.0)), float("{0:.2f}".format(b/256.0)), a
