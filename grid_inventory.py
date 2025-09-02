from constants import *
from data.item_data import item_data
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple
from scrollbar import ScrollBar
from utils.helper_functions import text_outline


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __mul__(self, other):
        return self.x * other, self.y * other

    def __rmul__(self, other):
        return self.x * other, self.y * other


class Item:
    def __init__(self, id: str) -> None:
        self.id = id
        self.name = item_data[id]["name"]
        self.item_type = item_data[id]["category"]
        self.width = item_data[id]["size"][0]
        self.height = item_data[id]["size"][1]
        self.stackable = item_data[id]["stackable"]
        self.max_stack = item_data[id]["max_stack"]
        self.stack_count = 1
        self.rotated = False
        self.highlighted = False
        self.selected = False

    def __repr__(self) -> str:
        return f"Item({self.id})"

    def copy(self) -> "Item":
        new_item = Item(self.id)
        new_item.stack_count = self.stack_count
        new_item.rotated = self.rotated
        return new_item

    def get_dimensions(self) -> Tuple[int, int]:
        """get item dimensions with consideration for rotation"""
        if self.rotated:
            return (self.height, self.width)
        return (self.width, self.height)

    def rotate(self):
        """rotate the item 90 degrees"""
        self.rotated = not self.rotated

    def can_stack_with(self, other: "Item") -> bool:
        """check if two items can stack"""
        if self == other:
            return False

        same_item_type = self.id == other.id
        both_stackable = self.stackable and other.stackable
        items_fit_in_one_stack = self.stack_count + other.stack_count <= self.max_stack

        return same_item_type and both_stackable and items_fit_in_one_stack


class GridSlot:
    def __init__(self):
        self.item: Optional[Item] = None
        self.occupied_by_item_at: Optional[Position] = None  # = points to topleft of item
        """
        no item: item = None and occupied_by_item_at = None
        item origin (topleft): item = Item  and occupied_by_item_at = None
        item: item = Item and occupied_by_item_at = Position(position of item origin)
        """

    def is_empty(self) -> bool:
        return self.item is None and self.occupied_by_item_at is None

    def is_item_origin(self):
        return self.item is not None and self.occupied_by_item_at is None


class GridInventory:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.changed = True

        # the inventory [2d Array]
        self.grid: List[List[GridSlot]] = [[GridSlot() for _ in range(width)] for _ in range(height)]
        # item position lookup
        self.items: Dict[Position, Item] = {}

    def is_valid_pos(self, x: int, y: int) -> bool:
        """check if pos is within grid bounds"""
        x_valid = 0 <= x < self.width
        y_valid = 0 <= y < self.height
        return x_valid and y_valid

    def can_place_item(self, item: Item, x: int, y: int, rotate_item: bool = False) -> bool:
        item_dimensions = item.get_dimensions()
        if not rotate_item:
            item_width, item_height = item_dimensions
        else:
            item_height, item_width = item_dimensions

        # check bounds:
        if not (self.is_valid_pos(x, y) and self.is_valid_pos(x + item_width - 1, y + item_height - 1)):
            return False

        # check if item slots are occupied:
        for dy in range(item_height):
            for dx in range(item_width):
                slot = self.grid[y + dy][x + dx]
                if not slot.is_empty():
                    # check if can stack item
                    if slot.is_item_origin():
                        if slot.item.can_stack_with(item):  # type:ignore
                            continue
                    else:
                        # check if item can stack at origin
                        item_origin = self.get_item_at(x, y)
                        if item_origin is not None and item_origin.can_stack_with(item):
                            continue

                    # check if item is item
                    if slot.item == item:
                        continue
                    # else return False
                    return False
        return True

    def place_item(self, item: Item, x: int, y: int, ammount: int = 0) -> bool:
        """place item at pos(x, y)"""
        if not self.can_place_item(item, x, y):
            return False

        # check for stacking at origin pos
        origin_slot = self.grid[y][x]
        if origin_slot is None:
            return False

        if origin_slot.is_item_origin() and origin_slot.item.can_stack_with(item):  # type:ignore
            origin_slot.item.stack_count += item.stack_count  # type:ignore
            return True

        # place new item
        item_width, item_height = item.get_dimensions()
        origin_pos = Position(x, y)

        # mark all occupied slots

        for dy in range(item_height):
            for dx in range(item_width):
                slot = self.grid[y + dy][x + dx]
                if dx == 0 and dy == 0:
                    # slot is item origin
                    slot.item = item
                    slot.occupied_by_item_at = None
                else:
                    # other slots occupied by item
                    slot.item = item
                    slot.occupied_by_item_at = origin_pos
        if ammount > 0:
            # if there should be a specified num of items placed
            # check if the ammout is equal or less than the items in this slot
            if ammount <= item.stack_count:
                item.stack_count = ammount

        self.items[origin_pos] = item
        return True

    def remove_item(self, x: int, y: int) -> Optional[Item]:
        """remove item at pos. (must be item origin)"""
        # check if pos is valid
        if not self.is_valid_pos(x, y):
            return None

        slot = self.grid[y][x]
        if not slot.is_item_origin:
            return None

        item = slot.item
        item_width, item_height = item.get_dimensions()  # type:ignore

        # clear all slots occupied by item
        for dy in range(item_height):
            for dx in range(item_width):
                clear_slot = self.grid[y + dy][x + dx]
                clear_slot.item = None
                clear_slot.occupied_by_item_at = None

        # remove from items dict
        del self.items[Position(x, y)]
        return item

    def move_item(self, origin_x: int, origin_y: int, target_x: int, target_y: int, rotate_item: bool = False, ammount: int = 0) -> bool:
        item = self.get_item_at(origin_x, origin_y)
        if item is None:
            return False
        # remove the clear the old grid slots
        item_origin = self.find_item_origin(origin_x, origin_y)
        if item_origin is None:
            return False
        # if the items to be moved var is 0 -> all items should be moved
        # or
        # if there is only one or null items to be moved
        # ---> remove the item
        # if not
        # ---> keep item. only reduce the stack
        stack_ammount_decreased = False
        if ammount == 0 or item.stack_count <= 1:
            self.remove_item(item_origin.x, item_origin.y)
        else:
            item.stack_count -= ammount
            stack_ammount_decreased = True

        rotated = False
        if rotate_item:
            item.rotate()
            rotated = True

        # if the item cannot be placed. place back at og pos

        if not self.place_item(item.copy(), target_x, target_y, ammount):
            if rotated:
                # if the item was rotated reset rotation
                item.rotate()

            self.place_item(item, item_origin.x, item_origin.y)

        return True

    def get_item_at(self, x: int, y: int) -> Optional[Item]:
        """Get item at position (works for any slot the item occupies)"""
        if not self.is_valid_pos(x, y):
            return None

        slot = self.grid[y][x]
        if slot.is_item_origin():
            return slot.item
        elif slot.occupied_by_item_at:
            origin_pos = slot.occupied_by_item_at
            return self.grid[origin_pos.y][origin_pos.x].item
        return None

    def find_item_origin(self, x: int, y: int) -> Optional[Position]:
        """Find the origin position of item at given coordinates"""
        slot = self.grid[y][x]
        if slot.is_item_origin():
            return Position(x, y)
        elif slot.occupied_by_item_at:
            return slot.occupied_by_item_at
        return None

    def auto_place_item(self, item: Item) -> Optional[Position]:
        """Try to automatically place item in first available spot"""
        for y in range(self.height):
            for x in range(self.width):
                if self.place_item(item, x, y):
                    return Position(x, y)
                else:  # try rotating the item
                    if self.try_rotate_and_place(item, x, y):
                        return Position(x, y)
        return None

    def auto_place_item_list(self, item_list: List[Item]) -> List[Optional[Item]]:
        placed_items: List[Optional[Item]] = []
        for item in item_list:
            if self.auto_place_item(item) is not None:
                placed_items.append(item)
        return placed_items

    def try_rotate_and_place(self, item: Item, x: int, y: int) -> bool:
        """Try placing item, and if failed, try rotating it"""
        if self.place_item(item, x, y):
            return True

        # Try rotating
        item.rotate()
        if self.place_item(item, x, y):
            return True

        # Rotate back if failed
        item.rotate()
        return False

    def get_all_items(self) -> List[Tuple[Position, Item]]:
        """Get all items with their positions"""
        return [(pos, item) for pos, item in self.items.items()]

    def print_grid(self):
        """Debug method to visualize the grid"""
        print("Grid Layout:")
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                slot = self.grid[y][x]
                if slot.is_item_origin():
                    row += f"[{slot.item.name[0]}]"  # type:ignore
                elif slot.occupied_by_item_at:
                    row += f" {slot.item.name[0]} "  # type:ignore
                else:
                    row += " . "
            print(row)


class GridInventoryViewport:
    def __init__(self, tilesize: int, height: int, inventory: GridInventory):
        self.inventory = inventory
        self.height = height
        self.grid_x = inventory.width
        self.grid_y = inventory.height
        self.tilesize = tilesize
        self.seperator_line = 1
        self.bg_color = (135, 86, 59)
        self.line_color = (145, 96, 69)
        self.line_color2 = (125, 76, 49)

        self.hover_surf_clear = pygame.Surface((self.tilesize, self.tilesize), pygame.SRCALPHA)
        self.hover_surf_clear.fill((255, 255, 255, 25))
        self.hover_surf_red = self.hover_surf_clear.copy()
        self.hover_surf_red.fill((255, 0, 0, 30))

        self.font = pygame.font.Font(join("assets", "font", "pixel_font.otf"), 10)
        self.text_color = (230, 230, 230)
        self.outline_color = (1, 1, 1)

        # for moving items
        self.selected_item: Optional[Item] = None
        self.rotate_selected_item: bool = False
        self.mouse_offset = (0, 0)
        self.item_origin_pos = (0, 0)
        self.dragging_item: bool = False
        self.item_ammount = 0  # 0 means take all

        self.offset_y: int = 0

        scrollbar_width = 10

        self.image = pygame.Surface((self.grid_x * self.tilesize + self.seperator_line + scrollbar_width, self.height))
        self.rect = self.image.get_rect()

        self.scrollbar = ScrollBar(scrollbar_width, self.image.get_height(), self.grid_y * self.tilesize, self.bg_color, self.line_color, self.rect.topright)

        self.redraw_surface()

    def get_item_under_mouse(self, rel_mouse_pos: tuple) -> Optional[Item]:
        grid_pos_x = rel_mouse_pos[0] // self.tilesize
        grid_pos_y = rel_mouse_pos[1] // self.tilesize

        item = self.inventory.get_item_at(grid_pos_x, grid_pos_y)
        if item is None:
            return None
        return item

    def get_grid_pos_from_mouse_pos(self, rel_mouse_pos: tuple):
        return rel_mouse_pos[0] // self.tilesize, rel_mouse_pos[1] // self.tilesize

    def draw_items(self):
        """draws all items on the surface (probably should only be called when inventory changed)"""
        # reset item surf
        self.redraw_surface()
        for pos, item in self.inventory.items.items():  # .items is a dict method that returns (key, value) unfortionate naming scheme lol
            # load the item img from item_data
            # check if item should be higlighted with outline
            if item.highlighted and not self.dragging_item:
                item_img = item_data[item.id]["image_outline"]
                # reset highlighted state (only display when mouse is over item)
                item.highlighted = False
            else:
                item_img = item_data[item.id]["image"]
            # if the item is selected by player draw it transparent
            if item.selected and item.stack_count > 1 and self.item_ammount > 0:
                item_img = item_data[item.id]["image"]
            elif item.selected:
                item_img = item_data[item.id]["image_alpha"]

            if item_img is None:
                print(f"WARNING! No item img found for item: {item.id}")
                # create replacement img
                item_width = item_data[item.id]["size"][0] * self.tilesize
                item_height = item_data[item.id]["size"][1] * self.tilesize
                item_img = pygame.Surface((item_width, item_height))
                item_img.fill("red")

            # rotate the item if its flaged as rotated
            if item.rotated:
                item_img = pygame.transform.rotate(item_img, 90.0)

            self.image.blit(item_img, pos * self.tilesize)
            self.draw_item_ammount_num(item, pos.x, pos.y)

    def redraw_surface(self):
        # redraw the grid
        self.image.fill(self.bg_color)
        for line in range(self.grid_x + 1):
            pygame.draw.line(self.image, self.line_color2, (line * self.tilesize - 1, 0), (line * self.tilesize - 1, self.rect.height), self.seperator_line)
            pygame.draw.line(self.image, self.line_color2, (line * self.tilesize + 1, 0), (line * self.tilesize + 1, self.rect.height), self.seperator_line)
            pygame.draw.line(self.image, self.line_color, (line * self.tilesize, 0), (line * self.tilesize, self.rect.height), self.seperator_line)
        for line in range(self.grid_y + 1):
            pygame.draw.line(self.image, self.line_color2, (0, line * self.tilesize - 1), (self.rect.width, line * self.tilesize - 1), self.seperator_line)
            pygame.draw.line(self.image, self.line_color2, (0, line * self.tilesize + 1), (self.rect.width, line * self.tilesize + 1), self.seperator_line)
            pygame.draw.line(self.image, self.line_color, (0, line * self.tilesize), (self.rect.width, line * self.tilesize), self.seperator_line)

    def draw_selected_item_at_cursor(self, rel_mouse_pos: tuple):
        """draws the item contained in the self.item_selected var at the curser with an offset
        to make 'picking up' an Item more organic. it also draws transparent squares at the pos
        where the item is going to be placed. white if the item fits and red if it doesnt!"""
        if self.selected_item is not None:
            # only run if item is being dragged
            # get item img from item_data file
            item_img = item_data[self.selected_item.id]["image_outline"]
            # get the pos the item is to be be drawn at. just the cursor pos + the dist to the item origin(topleft)
            pos_x = rel_mouse_pos[0] + self.mouse_offset[0]
            pos_y = rel_mouse_pos[1] + self.mouse_offset[1]
            # if the item is to be rotated after dragging: rotate the item img
            rotated = False
            if self.rotate_selected_item and self.selected_item.rotated:
                pass
            elif self.selected_item.rotated or self.rotate_selected_item:
                item_img = pygame.transform.rotate(item_img, 90)
                rotated = True

            # adust the grid pos for the placement indicators (trans squares) to be at the center of the item rather than the topleft
            grid_x, grid_y = self.get_grid_pos_from_mouse_pos((pos_x + self.tilesize // 2, pos_y + self.tilesize // 2))
            # draw white indicator when the item is placable at that location
            if self.inventory.can_place_item(self.selected_item, grid_x, grid_y, self.rotate_selected_item):
                hover_surf = self.hover_surf_clear
            # draw red indicator when it isnt
            else:
                hover_surf = self.hover_surf_red
            # loop for item size to create matching indicator rect
            for dy in range(item_img.get_width() // self.tilesize):
                for dx in range(item_img.get_height() // self.tilesize):
                    self.image.blit(hover_surf, ((grid_x + dy) * self.tilesize, (grid_y + dx) * self.tilesize))
            # blit the item img to the surf
            self.image.blit(item_img, (pos_x, pos_y))

    def draw_item_ammount_num(self, item: Item, x: int, y: int):
        if item.stack_count > 1 and not item.selected:
            width, height = item.get_dimensions()
            num_pos_x = x * self.tilesize + (width) * self.tilesize - 10
            num_pos_y = y * self.tilesize + (height) * self.tilesize - 10
            text = str(item.stack_count)

            text_surf = text_outline(self.font, text, self.text_color, self.outline_color)

            self.image.blit(text_surf, (num_pos_x, num_pos_y))

    def update(self, **kwargs):
        # get mouse button state
        mouse_buttons = pygame.mouse.get_pressed()
        # get the relative mouse pos
        rel_mouse_pos: tuple = kwargs["rel_mouse_pos"]
        # get the events (buttons mouse etc. for scrolling and keydown events)
        events = kwargs["events"]
        # get the item under the cursor
        item = self.get_item_under_mouse(rel_mouse_pos)
        # check if there was a item under the cursor
        if item is not None:
            # if there is highlight it with outline
            item.highlighted = True
            # if the player clicks at an item
            if (mouse_buttons[0] or mouse_buttons[2]) and not self.dragging_item:
                if mouse_buttons[2]:
                    self.item_ammount = 1
                # save the grid pos where the mouse got clicked
                self.item_origin_pos = self.get_grid_pos_from_mouse_pos(rel_mouse_pos)
                # get the item origin (topleft) of the item that got clicked
                item_origin = self.inventory.find_item_origin(self.item_origin_pos[0], self.item_origin_pos[1])
                # check if the item has an origin (why wouldnt it lol)
                if item_origin is not None:
                    # calc the mouse offset (dist from item topleft to rel mouse pos)
                    offset_x = item_origin.x * self.tilesize - rel_mouse_pos[0]
                    offset_y = item_origin.y * self.tilesize - rel_mouse_pos[1]
                    # save the offset for later item placing and dragging
                    self.mouse_offset = (offset_x, offset_y)
                    self.selected_item = item
                    self.rotate_selected_item = False
                    self.dragging_item = True

        if self.selected_item is not None:
            self.selected_item.selected = True
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.dragging_item:
                        self.rotate_selected_item = not self.rotate_selected_item
            if not (mouse_buttons[0] or mouse_buttons[2]) and self.selected_item:
                mouse_pos_x = rel_mouse_pos[0] + self.mouse_offset[0] + self.tilesize // 2
                mouse_pos_y = rel_mouse_pos[1] + self.mouse_offset[1] + self.tilesize // 2

                item_target_pos = self.get_grid_pos_from_mouse_pos((mouse_pos_x, mouse_pos_y))

                self.inventory.move_item(self.item_origin_pos[0], self.item_origin_pos[1], item_target_pos[0], item_target_pos[1], self.rotate_selected_item, self.item_ammount)
                self.selected_item.selected = False
                self.rotate_selected_item = False
                self.dragging_item = False
                self.selected_item = None
                self.item_ammount = 0

        self.draw_items()
        self.scrollbar.update(0)
        self.image.blit(self.scrollbar.image, self.scrollbar.rect)
        self.draw_selected_item_at_cursor(rel_mouse_pos)
