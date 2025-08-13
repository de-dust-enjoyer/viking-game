from constants import *

class Tile(pygame.sprite.Sprite):
	def __init__(self, pos:tuple, image:pygame.Surface, gid:int, layer_name:str):
		super().__init__()
		self.image:pygame.Surface = image
		self.rect = self.image.get_frect(topleft=pos)
		self.id = gid
		self.layer:str = layer_name
		self.cache = {}


	def scale_by(self, scale) -> pygame.Surface:
		if scale not in self.cache:
			self.cache[scale] = pygame.transform.scale_by(self.image, scale)
		return self.cache[scale]