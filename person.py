from constants import *

class Person:
    def __init__(self, name=None, attributes=None):
        '''name format = (forename, surname), attribute format = {category: {attribute: {stat: value}}}'''
        

        # base stats:
        self.damage = 5
        self.defense = 5
