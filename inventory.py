from constants import *
from base_classes.ui_element import UiElement
from item_grid_container import ItemGridContainer


class Inventory(UiElement):
    def __init__(self, parent, group: pygame.sprite.Group):
        self.player = parent.player
        elements = {
            "grid_container": ItemGridContainer(
                (167, 57),
                self.player.inventory,
                img=pygame.image.load(
                    join(
                        "assets", "sprites", "ui", "inventory", "grid_container_img.png"
                    )
                ).convert_alpha(),
            ),
            "item_info_box": ItemGridContainer(
                (13, 57),
                self.player.inventory,
                size=(147, 200),
            ),
        }
        img = pygame.image.load(
            join("assets", "sprites", "ui", "raid_menu", "background_surface.png")
        ).convert()
        super().__init__(
            parent,
            group,
            "inventory",
            (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2),
            img,
            True,
            **elements,
        )

    def update(self, dt):
        abs_mouse_pos = pygame.mouse.get_pos()
        mouse_x = (
            abs_mouse_pos[0]
            - self.rect.left
            - self.components["grid_container"].rect.left
        )
        mouse_y = (
            abs_mouse_pos[1]
            - self.rect.top
            - self.components["grid_container"].rect.top
        )
        item = self.components["grid_container"].get_item_by_mouse((mouse_x, mouse_y))
        self.update_components()

    def toggle_visibility(self):
        self.visible = not self.visible
