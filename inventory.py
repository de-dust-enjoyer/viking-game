from constants import *
from base_classes.ui_element import UiElement
from grid_inventory import GridInventory, GridInventoryViewport
from data.item_data import item_data


class Inventory(UiElement):
    def __init__(self, parent, group: pygame.sprite.Group):
        self.player = parent.player
        elements = {"grid_inventory": GridInventoryViewport((506, 74), INVENTORY_GRID_SIZE, 350, self.player.inventory)}

        img = pygame.image.load(join("assets", "sprites", "ui", "inventory", "background.png")).convert_alpha()
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
        text = "Ship Cargo Hold"
        font = pygame.font.Font(join("assets/font/pixel_font.otf"), 24)
        text_surf = font.render(text, False, (209, 171, 120))
        text_rect = text_surf.get_rect(center=(680, 48))
        self.image.blit(text_surf, text_rect)

    def update(self, dt, events):
        self.update_components(events)

    def toggle_visibility(self):
        self.visible = not self.visible
