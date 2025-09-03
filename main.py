from pygame import color
from constants import *
from utils.game_state_manager import GameStateManager
from world import World
from utils.debug_info import DebugInfo
from data.item_data import item_data, rarity_color
from utils.helper_functions import img_with_outline


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(GAME_TITLE)

        # game_state stuff
        self.game_state_manager = GameStateManager(STARTING_STATE)
        self.world = World(self.screen, self.game_state_manager, self)

        self.states = {"world": self.world}

        self.clock = pygame.time.Clock()

        self.debug_info = DebugInfo(pygame.font.Font(join("assets", "font", "Norse-Bold.otf"), 14))

        # load all item images
        for item in item_data:
            # get the image path with the item properties
            img_path = join("assets", "sprites", "items", str(item_data[item]["category"]), item + ".png")
            # load the image and convert it and scale it
            img = pygame.transform.scale_by(pygame.image.load(img_path).convert_alpha(), 2)
            item_data[item]["image"] = img
            item_data[item]["image_outline"] = img_with_outline(image=img, color=rarity_color[item_data[item]["rarity"]], line_thickness=2)
            item_data[item]["image_alpha"] = img.copy()  # need copy instead of pointer
            item_data[item]["image_alpha"].set_alpha(0)

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_TAB:
                        self.world.inventory_menu.toggle_visibility()

            # run the selected game state
            self.states[self.game_state_manager.get_state()].run(dt, events)

            # debugging osd
            self.debug_info.add("FPS", round(self.clock.get_fps(), 1))
            self.debug_info.add("selected_item", self.world.inventory_menu.components["grid_inventory"].selected_item)
            self.debug_info.add("rotate_selected_item", self.world.inventory_menu.components["grid_inventory"].rotate_selected_item)
            self.debug_info.add("item_ammount", self.world.inventory_menu.components["grid_inventory"].item_ammount)
            if self.world.inventory_menu.components["grid_inventory"].selected_item is not None:
                self.debug_info.add("stack_count", self.world.inventory_menu.components["grid_inventory"].selected_item.stack_count)

            # update the display surf
            self.debug_info.render(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
