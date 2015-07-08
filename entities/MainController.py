__author__ = 'dmartinez'

from pymongo import MongoClient
import time

class MainController:
	def __init__(self):
		self.name = "Main Controller"
		self.client = MongoClient('mongodb://ds049848.mongolab.com:49848')
		self.client.pystalker.authenticate('dandro', 'pyabc123')
		self.db = self.client.pystalker
		self.collection_logs = self.db.logs

	def output(self):
		print"Name: {}".format(self.name)

	def mongo_init(self):
		print"{}".format(self.collection_logs)

	def insert_new_log(self):
		log = {
			"start_time": time.asctime(),
			"project": "Test Insert",
			"description": "Trying to insert new row"
		}

		log_id = self.collection_logs.insert_one(log).inserted_id
		print"new Log ID: {}".format(log_id)
