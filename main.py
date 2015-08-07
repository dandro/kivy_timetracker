__author__ = 'dmartinez'

import kivy

kivy.require(kivy.__version__)

from kivy.app import App
from app import MainUI
from kivy.logger import Logger
from kivy.config import Config
from kivy.core.text import LabelBase

WINDOW_SIZE = 400, 768

# Window configuration
Config.set('graphics', 'width', WINDOW_SIZE[0])
Config.set('graphics', 'height', WINDOW_SIZE[1])
Config.set('graphics', 'fullscreen', 'fake')


class PyStalkerApp(App):
	icon = './assets/TimeTrackerApp_Logo.png'
	title = 'PyStalker'

	@staticmethod
	def load_fonts():
		LabelBase.register(name="fontawesome",
			fn_regular="assets/fonts/fontawesome-webfont.ttf")

	def build(self):
		self.load_fonts()
		return MainUI()

	# def on_start(self):
		# CALLBACK

	def on_stop(self):
		Logger.info('App: Aaaargh I\'m dying!')


if __name__ == '__main__':
	PyStalkerApp().run()
