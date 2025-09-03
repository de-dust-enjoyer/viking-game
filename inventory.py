from constants import *
from base_classes.ui_element import UiElement
from grid_inventory import GridInventory, GridInventoryViewport
from data.item_data import item_data


class Inventory(UiElement):
    def __init__(self, parent, group: pygame.sprite.Group):
        self.player = parent.player
        elements = {"grid_inventory": GridInventoryViewport(INVENTORY_GRID_SIZE, 300, self.player.inventory)}
        img = pygame.image.load(join("assets", "sprites", "ui", "inventory", "background_surface.png")).convert()
        super().__init__(
            parent,
            group,
            "inventory",
            (
                SCREEN_SIZE[0] // 2,
                SCREEN_SIZE[1] // 2,
            ),
            img,
            True,
            **elements
        )

    def update(self, dt, events):
        self.update_components(events)

    def toggle_visibility(self):
        self.visible = not self.visible
