from constants import *
from base_classes.ui_element import UiElement

class Inventory(UiElement):
    def __init__(self, parent, group:pygame.sprite.Group):
        super().__init__(self, parent, group, "inventory", (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2), True)