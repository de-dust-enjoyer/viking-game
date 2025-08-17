from constants import *

from person import Person

class Viking(Person):
	def __init__(self, name=None, attr={}):
		'''name format = (forename, surname), attribute format = {category: {attribute: {stat: value}}}'''
		Person.__init__(self, "viking", name, attr)
