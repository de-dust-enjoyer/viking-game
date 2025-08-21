from constants import *
from pygame_animation_player import Animation, AnimationPlayer


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, image: pygame.Surface, gid: int, layer_name: str):
        super().__init__()
        self.image: pygame.Surface = image
        self.rect = self.image.get_frect(topleft=pos)
        self.id = gid
        self.layer: str = layer_name

        self.cache = {}

    def scale_by(self, scale) -> pygame.Surface:
        w = int(round(self.rect.width * scale))  # type:ignore
        h = int(round(self.rect.height * scale))  # type:ignore

        key = int(round(scale * 100))  # e.g. 125 for 1.25×
        if key not in self.cache:
            self.cache[key] = pygame.transform.scale(self.image, (w, h))
        return self.cache[key]
