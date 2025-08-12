import constants
from game_state_manager import GameStateManager
from world import World

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode(constants.SCREEN_SIZE)
		pygame.display(constants.GAME_TITLE)

		# game_state stuff




	def run(self):
		for event in pygame.event.get():
			if event == pygame.QUIT:
				pygame.quit()
				sys.exit()

