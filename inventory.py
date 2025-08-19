from constants import *
from base_classes.ui_element import UiElement
from item_grid_container import ItemGridContainer

class Inventory(UiElement):
    def __init__(self, parent, group:pygame.sprite.Group):
        self.player = parent.player
        elements = {"grid_container": ItemGridContainer((40,40), self.player.inventory, size=(180,200))}
        img = pygame.image.load(join("assets", "sprites", "ui", "raid_menu", "background_surface.png")).convert()
        super().__init__(parent, group, "inventory", (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2), img, True, **elements)

    def update(self, dt):

        self.update_components()