__author__ = 'dmartinez'

import kivy

kivy.require(kivy.__version__)

from kivy.app import App
from entities import MainUI
from kivy.logger import Logger
from kivy.config import Config

WINDOW_SIZE = 400, 768

# Window configuration
Config.set('graphics', 'width', WINDOW_SIZE[0])
Config.set('graphics', 'height', WINDOW_SIZE[1])
Config.set('graphics', 'fullscreen', 'fake')


class PyStalkerApp(App):
	icon = './assets/TimeTrackerApp_Logo.png'
	title = 'PyStalker'

	def build(self):
		return MainUI()

	# def on_start(self):
		# CALLBACK

	def on_stop(self):
		Logger.info('App: Aaaargh I\'m dying!')


if __name__ == '__main__':
	PyStalkerApp().run()