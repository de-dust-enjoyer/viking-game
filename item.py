from constants import *


class Item:
    def __init__(self, id):
        self.id = id
        og_img = pygame.image.load(
            join("assets", "sprites", "items", self.id + ".png")
        ).convert_alpha()
        self.image = pygame.transform.scale_by(og_img, 2)
        self.rect = self.image.get_rect()
