from constants import *

class Object(pygame.sprite.Sprite):
	def __init__(self, name:str, layer_name:str):
		super().__init__()
		self.id = name
		self.layer_name = layer_name
		self.dead = False
		self.image = pygame.Surface((16,16))
		self.flip_h = False

	def scale_by(self, scale:float) -> pygame.Surface:
		scaled_img = pygame.transform.scale_by(self.image, scale) # type:ignore
		return pygame.transform.flip(scaled_img, self.flip_h, False)

        