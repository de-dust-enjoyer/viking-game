from pygame import event
from constants import *


class UiElement(pygame.sprite.Sprite):
    def __init__(self, parent, group: pygame.sprite.Group, id: str, pos: tuple, background_surf: pygame.Surface, centered=False, **kwargs) -> None:
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

    def update(self, dt, events):
        self.update_components(events)

    def update_components(self, events):
        for component in self.components.values():
            component.visible = self.visible
            if component.visible:
                component.update(
                    rel_mouse_pos=(
                        pygame.mouse.get_pos()[0] - self.rect.left - component.rect.left,
                        pygame.mouse.get_pos()[1] - self.rect.top - component.rect.top,
                    ),
                    events=events,
                )

                # blit componets to background surf
                self.image.blit(component.image, component.rect)  # type:ignore

    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

    def is_visible(self):
        return self.visible
