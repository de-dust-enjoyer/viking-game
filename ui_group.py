from constants import *

class UiGroup(pygame.sprite.Group):
    """ui grouuuup"""
    def __init__(self):
        super().__init__()
        



    def draw(self, surface:pygame.Surface):
        for sprite in self.sprites():
            if sprite.visible:
                surface.blit(sprite.image, sprite.rect)
