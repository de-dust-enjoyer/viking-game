from constants import *
from typing import Optional

class Object(pygame.sprite.Sprite):
	def __init__(self, name:str, layer_name:str, group:pygame.sprite.Group):
		super().__init__(group)
		self.id = name
		self.group = group
		self.layer_name = layer_name
		self.dead = False
		self.image:Optional[pygame.Surface] = None
		self.flip_h = False

	def scale_by(self, scale:float) -> pygame.Surface:
		scaled_img = pygame.transform.scale_by(self.image, scale)
		return pygame.transform.flip(scaled_img, self.flip_h, False)

        