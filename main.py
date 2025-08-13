from constants import *
from game_state_manager import GameStateManager
from world import World

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

	def run(self):
		while True:
			dt = self.clock.tick() / 1000
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()


			# run the selected game state
			self.states[self.game_state_manager.get_state()].run(dt)

			# update the display surf
			pygame.display.flip()


if __name__ == "__main__":
	game = Game()
	game.run()