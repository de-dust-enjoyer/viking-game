from constants import *


class ScrollBar:
    def __init__(self, width, visible_size, total_size, bg_color, fg_color, pos: tuple = (0, 0)):
        self.width = width
        self.visible_size = visible_size
        self.total_size = total_size
        self.thumb_height = int(visible_size / total_size * visible_size)
        self.progress: int = 0  # 0-100
        self.offset = 0
        self.thumb_rect = pygame.Rect(0, round(visible_size / 100 * self.progress), self.width, self.thumb_height)

        self.image = pygame.Surface((self.width, visible_size))
        self.image.fill(bg_color)
        self.rect = self.image.get_rect(topright=pos)
        self.thumb = pygame.Surface((self.width, self.thumb_height))
        self.thumb.fill(fg_color)

        self.image.blit(self.thumb, self.thumb_rect)

    def update(self, new_offset: int):
        if new_offset == self.offset:
            return
        self.offset = new_offset

        new_progress = self.get_progress_from_offset(new_offset)
        self.progress = new_progress
        self.thumb_rect.top = round(self.visible_size / 100 * self.progress)

        self.image.blit(self.thumb, self.thumb_rect)

    def get_progress_from_offset(self, offset: int) -> int:
        return round(100 / self.total_size * offset)
