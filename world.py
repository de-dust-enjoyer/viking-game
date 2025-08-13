from constants import *
from camera import CameraGroup
from player_ship import PlayerShip
from tile import Tile

import pytmx

class World:
	def __init__(self, screen, game_state_manager, game):
		self.screen = screen
		self.game_state_manager = game_state_manager
		self.game = game

		# chunking
		self.chunked_tiles = {} # {(chunk_x, chunk_y): [Tile, Tile, Tile ...]}

		# groups
		self.objects = pygame.sprite.Group()
		self.all_tiles = pygame.sprite.Group()
		self.collision_tiles = pygame.sprite.Group()
		self.camera_group = CameraGroup([self.objects], self.chunked_tiles, CHUNK_SIZE)
		self.ui_group = pygame.sprite.Group()

		self.player = PlayerShip((SCREEN_SIZE[0]//2,SCREEN_SIZE[1]//2), "player", "viking_ship_01", "ships")
		self.objects.add(self.player)
		self.camera_group.set_target(self.player, permanent=True)

		self.build_world()

	def run(self, dt:float):
		# input

		# logic
		for obj in self.objects:
			obj.update(dt)
		
		self.ui_group.update(dt)

		# rendering
		self.camera_group.custom_draw()
		self.ui_group.draw(self.screen)







	def build_world(self):
		tmx_data = pytmx.util_pygame.load_pygame(join("assets", "tiled", "levels", "world_map.tmx")) # type:ignore
		for layer in tmx_data.visible_layers:
			if isinstance(layer, pytmx.TiledTileLayer):
				for x, y, gid in layer: #type:ignore
					tile_img = tmx_data.get_tile_image_by_gid(gid)
					if not tile_img:
						continue
				
					pos = (x * TILE_SIZE[0], y * TILE_SIZE[1])

					tile = Tile(pos, tile_img, gid, layer.name)
					self.all_tiles.add(tile)


				# chunking

					chunk_x = pos[0] // CHUNK_SIZE
					chunk_y = pos[1] // CHUNK_SIZE
					chunk_key = (chunk_x, chunk_y)
					self.chunked_tiles.setdefault(chunk_key, []).append(tile)



		
