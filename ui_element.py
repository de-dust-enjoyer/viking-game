from constants import *
from typing import Optional

class UiElement(pygame.sprite.Sprite):
    def __init__(self, parent, group:pygame.sprite.Group, id:str, pos:tuple, background_surf:pygame.Surface, centered=False, **kwargs) -> None:
        """kwargs is ui components only!!!"""
        pygame.sprite.Sprite.__init__(self, group)
        self.group = group
        self.parent = parent
        self.id = id
        self.image = background_surf
        if centered:
            self.rect: pygame.Rect = self.image.get_rect(center=pos)
        else:
            self.rect: pygame.Rect = self.image.get_rect(topleft=pos)
        self.components = kwargs



        self.visible = True

    def update(self, dt):
        for component in self.components:
            self.components[component].visible = self.visible
            if self.components[component].visible:
                self.components[component].update(rel_mouse_pos=(pygame.mouse.get_pos()[0] - self.rect.left, pygame.mouse.get_pos()[1] - self.rect.top))
                # blit componets to background surf
                self.image.blit(self.components[component].image, self.components[component].rect) # type:ignore
            



    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

    def is_visible(self):
        return self.visible


