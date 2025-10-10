from constants import *
from data.item_data import item_data
import random


class Item(pygame.sprite.Sprite):
    def __init__(self, id: str, pos: tuple, group: pygame.sprite.Group):
        super().__init__(group)
        self.id = id
        self.image: pygame.Surface = item_data[id]["image_drop"]
        self.rect: pygame.FRect = self.image.get_frect(center=pos)
        self.velocity = pygame.Vector2(random.randint(0, 100), random.randint(0, 100))
        self.dead = False
        self.cache = {}

    def update(self, dt):
        self.velocity = self.velocity.lerp(pygame.Vector2(0, 0), 0.01)
        self.rect.center += self.velocity * dt

    def scale_by(self, scale):
        if scale not in self.cache:
            self.cache[scale] = pygame.transform.scale_by(self.image, scale)
        return self.cache[scale]
