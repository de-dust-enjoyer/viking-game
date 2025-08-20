from constants import *
from utils.game_state_manager import GameStateManager
from world import World
from utils.debug_info import DebugInfo


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

        self.debug_info = DebugInfo(
            pygame.font.Font(join("assets", "font", "Norse-Bold.otf"), 14)
        )

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
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
            self.states[self.game_state_manager.get_state()].run(dt)

            # debugging osd
            self.debug_info.add("FPS: ", round(self.clock.get_fps(), 1))
            self.debug_info.add(
                "Sprites Rendered: ", self.world.camera_group.sprites_drawn
            )
            self.debug_info.add("Player Pos: ", self.world.player.rect.center)

            # update the display surf
            self.debug_info.render(self.screen)
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
