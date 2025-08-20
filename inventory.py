from constants import *
from base_classes.ui_element import (
    UiElement,
)
from item_grid_container import (
    ItemGridContainer,
)
from text_display import (
    TextDisplay,
)
from data.item_data import (
    item_data,
)
import textwrap


class Inventory(UiElement):
    def __init__(
        self,
        parent,
        group: pygame.sprite.Group,
    ):
        self.player = parent.player
        elements = {
            "grid_container": ItemGridContainer(
                (
                    167,
                    57,
                ),
                self.player.inventory,
                img=pygame.image.load(
                    join(
                        "assets",
                        "sprites",
                        "ui",
                        "inventory",
                        "grid_container_img.png",
                    )
                ).convert_alpha(),
            ),
            "item_info_box": TextDisplay(
                (
                    13,
                    57,
                ),
                pygame.image.load(
                    join(
                        "assets",
                        "sprites",
                        "ui",
                        "inventory",
                        "item_info_box_img.png",
                    )
                ).convert_alpha(),
                pygame.font.Font(
                    join(
                        "assets",
                        "font",
                        "pixel_font.otf",
                    ),
                    10,
                ),
                (
                    10,
                    10,
                    10,
                ),
            ),
        }
        img = pygame.image.load(
            join(
                "assets",
                "sprites",
                "ui",
                "inventory",
                "background_surface.png",
            )
        ).convert()
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
            **elements,
        )

    def update(
        self,
        dt,
    ):
        abs_mouse_pos = pygame.mouse.get_pos()
        mouse_x = abs_mouse_pos[0] - self.rect.left - self.components["grid_container"].rect.left
        mouse_y = abs_mouse_pos[1] - self.rect.top - self.components["grid_container"].rect.top
        item = self.components["grid_container"].get_item_by_mouse(
            (
                mouse_x,
                mouse_y,
            )
        )
        if item:
            text_list = []
            text_list.extend(
                textwrap.fill(
                    item_data[item[0]]["name"].upper(),
                    15,
                ).splitlines()
            )
            text_list.append(" ")
            text_list.extend(
                textwrap.fill(
                    f"amount {item[1]}x",
                    20,
                ).splitlines()
            )
            text_list.extend(textwrap.fill(f"{item_data[item[0]]['value']}x{item[1]} = {item_data[item[0]]['value'] * item[1]}").splitlines())
            text_list.extend(
                textwrap.fill(
                    f"{item_data[item[0]]['rarity']} item",
                    15,
                ).splitlines()
            )
            text_list.append(" ")
            text_list.extend(
                textwrap.fill(
                    item_data[item[0]]["description"],
                    15,
                ).splitlines()
            )

            self.components["item_info_box"].display_text(*text_list)
        self.update_components()

    def toggle_visibility(
        self,
    ):
        self.visible = not self.visible
