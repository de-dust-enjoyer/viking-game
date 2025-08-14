from constants import *
import names
import attributes
from person import Person

class Viking(Person):
	def __init__(self, name=None, attr=None):
		'''name format = (forename, surname), attribute format = {category: {attribute: {stat: value}}}'''
		Person.__init__(self, name, attr)
		if name:
			self.forename, self.surname = name
		else:
			self.forename, self.surname = names.generate_name(names.viking_names)
		if attr:
			self.attributes = attr
		else:
			self.attributes = attributes.get_random_attributes(attributes.viking_attributes)

		# base stats:
		self.damage = 5
		self.defense = 5

		# stat bonuses from attributes
		for category in self.attributes:
			for attribute in self.attributes[category]:
				for stat in self.attributes[category][attribute]:
					if stat == "damage":
						self.damage += self.attributes[category][attribute][stat]
						self.damage = 0 if self.damage < 0 else self.damage
					elif stat == "defense":
						self.defense += self.attributes[category][attribute][stat]
						self.defense = 0 if self.defense < 0 else self.defense


	def print_info(self):
		print("-----------------------------------")
		print(f"hi my name is {self.forename} {self.surname}.")
		for category in self.attributes:
			for attribute in self.attributes[category]:
				print(viking_attributes.attribute_info[attribute])

		print(f"my damage is {self.damage}")
		print(f"my defense is {self.defense}")
		print("-----------------------------------")

	def get_stat(self, stat) -> int:
		if stat == "damage":
			return self.damage
		elif stat == "defense":
			return self.defense
		else:
			return 0
