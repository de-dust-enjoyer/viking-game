from constants import *
import viking_names

class Viking:
	def __init__(self, name=None, attributes=None):
		'''name format = (forename, surname)'''
		if name:
			self.forename, self.surname = name
		else:
			self.forename, self.surname = viking_names.generate_name(viking_names.names)
		print(self.forename, self.surname)
viking = Viking()