from constants import *
from pygame_animation_player import Animation, AnimationPlayer
from utils.timer import Timer


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

    def increment_frame(self):
        self.frame_index += 1
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def scale_by(self, scale) -> pygame.Surface:
        if scale not in self.cache[self.frame_index]:
            self.cache[self.frame_index][scale] = pygame.transform.scale_by(self.frames[self.frame_index], scale)
        return self.cache[self.frame_index][scale]


class TileAnimationManager:
    def __init__(self):
        self.groups = {}  # {frame_duration: [tile, tile, tile, ...]}
        self.timers = {}  # {frame_duration: Timer object}
        self.ready = False

    def init(self, chunked_tiles) -> None:
        self.groups = {}
        for chunk in chunked_tiles.values():
            for tile in chunk:
                if tile.frame_duration not in self.groups:
                    # group with frame duration does not jet exist -> create group
                    self.groups[tile.frame_duration] = []
                    # also need a timer for every group (repeat true because of course)
                    self.timers[tile.frame_duration] = Timer(tile.frame_duration, repeat=True)
                    # need to start the timer
                    self.timers[tile.frame_duration].start()
                    # add tile to group
                    self.groups[tile.frame_duration].append(tile)
                else:
                    # group with frame duration does already exist -> add tile to group
                    self.groups[tile.frame_duration].append(tile)
        self.ready = True
        self.start_all_timers()

    def update(self) -> None:
        # only update if self.init has been called at least once
        if self.ready:
            for duration in self.timers:
                if self.timers[duration].update():
                    for tile in self.groups[duration]:
                        tile.increment_frame()

    def start_all_timers(self) -> None:
        for timer in self.timers.values():
            timer.start()
