from pygame import color
from constants import *
from level import Level
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
        self.level = Level(self.screen, self.game_state_manager, self)

        self.states = {"world": self.world, "level": self.level}

        self.clock = pygame.time.Clock()

        self.debug_info = DebugInfo(pygame.font.Font(join("assets", "font", "Norse-Bold.otf"), 14))
        color = "#FFFFFF"
        # load all item images
        for item in item_data:
            # get the image path with the item properties
            img_path_inventory = join("assets", "sprites", "items_inventory", str(item_data[item]["category"]), item + ".png")
            img_path_drop = join("assets", "sprites", "items_drop", str(item_data[item]["category"]), item + ".png")
            # load the image and convert it and scale it
            img = pygame.transform.scale_by(pygame.image.load(img_path_inventory).convert_alpha(), 2)
            item_data[item]["image"] = img
            item_data[item]["image_outline"] = img_with_outline(image=img, color=rarity_color[item_data[item]["rarity"]], line_thickness=2)
            item_data[item]["image_alpha"] = img.copy()  # need copy instead of pointer
            item_data[item]["image_alpha"].set_alpha(0)
            item_data[item]["image_drop"] = pygame.transform.scale_by(pygame.image.load(img_path_inventory).convert_alpha(), 0.5)

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
                elif event.type == pygame.MOUSEWHEEL:
                    if self.game_state_manager.get_state()[0] == "level":
                        self.level.camera_group.zoom += event.y

            # run the selected game state
            state, level = self.game_state_manager.get_state()
            if level is not None:
                self.level.town = self.world.player.raid_target  # type:ignore
            self.states[state].run(dt, events)

            # debugging osd

            # update the display surf
            self.debug_info.render(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
