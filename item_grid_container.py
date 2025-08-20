from constants import *
from data.item_data import item_data
from item import Item
from utils.helper_functions import text_outline


class ItemGridContainer:
    """its a ui component"""

    def __init__(self, pos: tuple, item_list: list, **kwargs):
        self.item_list = item_list
        self.clean_item_list = []
        self.item_count_dict = {}
        self.visible = True

        self.font = pygame.font.Font(join("assets", "font", "pixel_font.otf"), 10)

        if len(item_list) > 0:
            self.item_img_size = item_list[0].image.get_width()
        else:
            self.item_img_size = 16

        self.spacing = 4
        self.padding = 6

        self.scroll_offset = 0

        # random value. gets changed anyways if not raises error!
        self.image = pygame.Surface((1, 1))
        for attr in kwargs:
            if (
                attr == "image"
                or attr == "background"
                or attr == "background_img"
                or attr == "img"
                or attr == "background_image"
            ):
                if isinstance(kwargs[attr], pygame.Surface):
                    self.image = kwargs[attr]
            elif attr == "size":
                if type(kwargs[attr]) == tuple:
                    self.image = pygame.Surface(kwargs[attr], pygame.SRCALPHA)
                    self.image.fill((20, 20, 20, 30))

        self.rect = self.image.get_rect(topleft=pos)
        self.grid_surf = pygame.Surface(
            (self.rect.width - self.padding * 2, self.rect.height - self.padding * 2),
            pygame.SRCALPHA,
        )
        self.grid_rect = self.grid_surf.get_rect(
            center=(self.rect.width // 2, self.rect.height // 2)
        )
        self.items_per_row = 0
        self._refresh_item_counts()
        self._draw_items()

    def update(self, rel_mouse_pos: tuple) -> None:
        self._draw_items()

    def _calculate_grid_position(self, index: int) -> tuple:
        self.items_per_row = (self.grid_rect.width + self.spacing) // (
            self.item_img_size + self.spacing
        )
        if self.items_per_row == 0:
            raise ZeroDivisionError(
                f"container width: {self.grid_rect.width} is smaller than item img size: {self.item_img_size + self.spacing}"
            )
        row = index // self.items_per_row
        col = index % self.items_per_row

        return col * (self.item_img_size + self.spacing), row * (
            self.item_img_size + self.spacing
        )

    def _is_item_visible(self, index: int) -> bool:
        y = self._calculate_grid_position(index)[1]
        item_bottom = y + self.item_img_size

        return y < self.grid_rect.height and item_bottom > 0

    def _refresh_item_counts(self) -> None:
        """very expensive method dont use every frame"""
        # reset the item counts
        self.item_count_dict = {}

        for item in self.item_list:
            # check if there is alredy the same item in the dict
            if item.id in self.item_count_dict:
                self.item_count_dict[item.id] += 1

            else:
                self.item_count_dict[item.id] = 1
                self.clean_item_list.append(item)

    def _draw_items(self) -> None:
        for index, item in enumerate(self.clean_item_list):
            x, y = self._calculate_grid_position(index)
            self.grid_surf.blit(item.image, (x, y))
            if self.item_count_dict[item.id] > 1:
                # blit num of items
                self.grid_surf.blit(
                    text_outline(
                        self.font,
                        str(self.item_count_dict[item.id]),
                        (255, 255, 255),
                        # cannot be (0,0,0) because colorkey is (0,0,0)
                        (1, 1, 1),
                    ),
                    (x + 20, y + 20),
                )
        self.image.blit(self.grid_surf, self.grid_rect)

    def get_item_by_mouse(self, rel_mouse_pos):
        if self.visible:
            mouse_x = rel_mouse_pos[0] - self.padding
            mouse_y = rel_mouse_pos[1] - self.padding

            grid_x = mouse_x // (self.item_img_size + self.spacing)
            grid_y = mouse_y // (self.item_img_size + self.spacing)

            if self.grid_rect.collidepoint((mouse_x, mouse_y)):
                index = self._get_item_index((grid_x, grid_y))
                if index < len(self.clean_item_list) and index >= 0:
                    name = self.clean_item_list[index].id
                    quantity = self.item_count_dict[name]

                    return name, quantity, index
        return

    def _get_item_index(self, grid_pos: tuple):
        index = self.items_per_row * grid_pos[1] + grid_pos[0]
        return index
