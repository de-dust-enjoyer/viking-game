from constants import *
import names
import attributes

class Person:
    def __init__(self, type:str, name=None, attr=None):
        '''name format = (forename, surname), attribute format = {category: {attribute: {stat: value}}}'''
        self.type = type
        if name:
            self.forename, self.surname = name
        else:
            self.forename, self.surname = names.generate_name(names.forenames, names.surnames, self.type)
        if attr:
            self.attributes = attr
        else:
            self.attributes = attributes.get_random_attributes(attributes.attributes, self.type)

        # base stats:
        self.base_damage = 5
        self.base_defense = 5
        self.base_health = 30
        self.damage = self.base_damage
        self.defense = self.base_defense
        self.health = self.base_health

        self.refresh_attr_boni()

        self.print_info()

    


    def refresh_attr_boni(self):
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
                print(attributes.attribute_dialog[self.type][attribute])
        print(f"my damage is {self.damage}")
        print(f"my defense is {self.defense}")
        print("-----------------------------------")

    def get_stat(self, stat) -> int:
        if stat == "damage":
            return self.damage
        elif stat == "defense":
            return self.defense
        elif stat == "health":
            return self.health
        else:
            return 0

