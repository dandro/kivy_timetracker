__author__ = 'dmartinez'

from kivy.logger import Logger
import time


class TimeParser(object):
	def __init__(self, db_dict):
		self.db_dict = db_dict

	def parse_rows(self):
		report_data = {}
		data = self.get_all_rows(self.db_dict)
		for i in range(0, len(data)):
			current_row = data[i]
			row_duration = self.get_row_duration(data, i)
			self.group_logs(report_data, current_row) if current_row['project_title'] in report_data else \
				self.add_new_log(report_data, current_row)

	@staticmethod
	def get_row_duration(data, i):
		current_time = time.strptime(data[i]['time'], '%Y-%m-%d %H:%M:%S')
		next_time = time.strptime(data[i + 1]['time'], '%Y-%m-%d %H:%M:%S')
		return 0

	@staticmethod
	def get_all_rows(db):
		report_data = []
		for key in db.getall():
			report_data.append(db.get(key))
		return report_data

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
