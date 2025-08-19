from constants import *
from data.item_data import item_data
from item import Item

class ItemGridContainer:
    """its a ui component"""
    def __init__(self, pos:tuple, item_list:list, **kwargs):
        self.item_list = item_list
        self.clean_item_list = []
        self.item_count_dict = {}

        self.item_img_size = 16

        self.spacing = 4
        self.padding = 5

        self.scroll_offset = 0
        self.image = pygame.Surface((1, 1)) # random value. gets changed anyways if not raises error!
        for attr in kwargs:
            if attr == "image" or attr == "background" or attr == "background_img":
                if isinstance(kwargs[attr], pygame.Surface):
                    self.image = kwargs[attr]
            elif attr == "size":
                if type(kwargs[attr]) == tuple:
                    self.image = pygame.Surface(kwargs[attr], pygame.SRCALPHA)


        self.rect = self.image.get_rect(topleft=pos)
        self.grid_surf = pygame.Surface((self.rect.width - self.padding * 2, self.rect.height - self.padding * 2), pygame.SRCALPHA)
        self.grid_rect = self.grid_surf.get_rect(center= (self.rect.width//2, self.rect.height//2))


        self._refresh_item_counts()
        self._draw_items()


        
    def update(self, rel_mouse_pos:tuple) -> None:
        self._draw_items()

    def _calculate_grid_position(self, index:int) -> tuple:


        items_per_row = (self.grid_rect.width + self.spacing) // (self.item_img_size + self.spacing)
        if items_per_row == 0:
            raise ZeroDivisionError(f"container width: {self.grid_rect.width} is smaller than item img size: {self.item_img_size + self.spacing}")
        row = index // items_per_row
        col = index % items_per_row

        return col * (self.item_img_size + self.spacing), row * (self.item_img_size + self.spacing)

    def _is_item_visible(self, index:int) -> bool:
        y = self._calculate_grid_position(index)[1]
        item_bottom = y + self.image_size

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

        self.clean_item_list = list(set(self.item_list))

    def _draw_items(self) -> None:
        for index, item in enumerate(self.clean_item_list):
            x, y = self._calculate_grid_position(index)
            self.grid_surf.blit(item.image, (x, y))
        self.image.blit(self.grid_surf, self.grid_rect)