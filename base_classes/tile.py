from constants import *
from pygame_animation_player import Animation, AnimationPlayer


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, image: pygame.Surface, gid: int, layer_name: str):
        super().__init__()
        self.image: pygame.Surface = image
        self.rect = self.image.get_rect(topleft=pos)
        self.id = gid
        self.layer: str = layer_name

        self.cache = {}

    def scale_by(self, scale) -> pygame.Surface:
        if scale not in self.cache:
            self.cache[scale] = pygame.transform.scale_by(self.image, scale)
        return self.cache[scale]


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
        self.cache = []
        for frame in range(len(frames)):
            self.cache.append({})

    def update(self, dt):
        if not self.is_animated:
            return

        self.animation_timer += dt

        if self.animation_timer >= self.frame_duration:
            self.frame_index += 1
            self.animation_timer = 0

            if self.frame_index >= len(self.frames):
                self.frame_index = 0
            self.image = self.frames[self.frame_index]

    def scale_by(self, scale) -> pygame.Surface:
        if scale not in self.cache[self.frame_index]:
            self.cache[self.frame_index][scale] = pygame.transform.scale_by(self.frames[self.frame_index], scale)
        return self.cache[self.frame_index][scale]
