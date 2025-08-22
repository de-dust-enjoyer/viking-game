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


class AnimatedTile(Tile):
    def __init__(self, pos: tuple, frames: list, frame_duration: float, gid: int, layer_name: str):
        if not frames:
            raise ValueError(f"frames for tile with gid {gid} is empty")
        Tile.__init__(self, pos, frames[0], gid, layer_name)

        self.frames = frames
        self.frame_duration = frame_duration / 1000  # in seconds
        self.animation_timer = 0
        self.is_animated = len(frames) > 1
        self.frame_index = 0
        self.cache = [{}]

    def update(self, dt):
        if not self.is_animated:
            return

        self.animation_timer += dt

        if self.animation_timer >= self.frame_duration:
            self.frame_index += 1
            self.animation_timer = 0

            self.image = self.frames[self.frame_index]
            if self.frame_index >= len(self.frames):
                self.frame_index = 0

    def scale_by(self, scale) -> pygame.Surface:
        if scale not in self.cache[self.frame_index]:
            self.cache[self.frame_index][scale] = pygame.transform.scale_by(self.frames[self.frame_index], scale)
        return self.cache[self.frame_index][scale]
