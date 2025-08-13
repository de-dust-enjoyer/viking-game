from constants import *
from object import Object

class Town(Object):
    def __init__(self, image:pygame.Surface, pos:tuple, id:str, layer_name:str, attributes:dict, landing_zones:dict):
        Object.__init__(self, id, layer_name)
        self.image = image
        self.rect = self.image.get_frect(center= pos)
        self.attributes = attributes
        print(landing_zones[self.id])

