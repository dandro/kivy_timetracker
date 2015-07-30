__author__ = 'dmartinez'

from kivy.logger import Logger


class TimeParser(object):
	def __init__(self, db_dict):
		self.db_dict = db_dict

	def parse_rows(self):
		report_data = {}
		for key in self.db_dict.getall():
			current_row = self.db_dict.get(key)
			self.group_logs(report_data, current_row) if current_row['project_title'] in report_data else \
				self.add_new_log(report_data, current_row)

	@staticmethod
	def group_logs(report_data, current_row):
		report_data[current_row['project_title']]['time'] += ', ' + current_row['time']
		report_data[current_row['project_title']]['project_description'] += ', ' + current_row['project_description']

	@staticmethod
	def add_new_log(report_data, current_row):
		report_data[current_row['project_title']] = {
			'time': current_row['time'],
			'project_description': current_row['project_description']
		}
