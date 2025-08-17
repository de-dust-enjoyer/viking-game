from constants import *

from person import Person

class Soldier(Person):
    def __init__(self, name=None, attr=None):
        '''name format = (forename, surname), attribute format = {category: {attribute: {stat: value}}}'''
        Person.__init__(self, "english", name, attr)