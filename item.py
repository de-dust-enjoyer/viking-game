from constants import *

class Item:
    def __init__(self, id):
        self.id = id
        self.image = pygame.image.load(join("assets", "sprites", "items", self.id + ".png")).convert_alpha()