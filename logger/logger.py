
class Logger():
	def __init__(self, dest):
		self.file = open(dest, 'wb+')

	def write(self, line):
		self.file.write(line + '\n')

	def end(self):
		self.file.close()
