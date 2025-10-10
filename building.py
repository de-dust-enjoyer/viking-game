from constants import *
from base_classes.object import Object


class Building(Object):
    def __init__(self, image: pygame.Surface, pos: tuple, id: str, layer_name: str, group: pygame.sprite.Group):
        super().__init__(id, layer_name, group)
        self.id = id
        self.health = 100
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, dt):
        pass
