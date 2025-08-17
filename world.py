from constants import *
from camera import CameraGroup
from ui_group import UiGroup
from player_ship import PlayerShip
from base_classes.tile import Tile
from town import Town
from button import Button
from raid_menu import RaidMenu

import pytmx

class World:
	def __init__(self, screen, game_state_manager, game):
		self.screen = screen
		self.game_state_manager = game_state_manager
		self.game = game

		# chunking
		self.chunked_tiles = {} # {(chunk_x, chunk_y): [Tile, Tile, Tile ...]} # for collisions
		self.chunked_tile_imgs = {} # {(chunk_x, chunk_y): BIG_TILE} # for rendering

		self.world_size = (0,0)
		self.tilesize = (0,0)


		# groups
		self.objects = pygame.sprite.Group()
		self.camera_group = CameraGroup(self.screen, [self.objects], self.chunked_tile_imgs, CHUNK_SIZE)
		self.ui_group = UiGroup()

		self.player = PlayerShip((10000,14000), "player", "viking_ship_01", "ships", self.objects)
		self.camera_group.set_target(self.player, permanent=True)

		self.build_world()

		# ui elements:

		self.raid_menu = RaidMenu(self, self.ui_group, "raid_menu", (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2 - 100), 
			pygame.image.load("assets/sprites/ui/raid_menu/background_surface.png").convert_alpha(), centered=True)

			



#------------------------------------------------------------------------------------------------------------------------------------------------------------------
	def run(self, dt:float):
		# input

		# logic
		for obj in self.objects:
			obj.update(dt)

		self.ui_group.update(dt)

		# rendering
		self.camera_group.custom_draw()
		self.ui_group.draw(self.screen)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------




	def build_world(self):
		tmx_data = pytmx.util_pygame.load_pygame(join("assets", "tiled", "levels", "test_world.tmx")) # type:ignore
		self.tilesize = (tmx_data.tilewidth, tmx_data.tileheight)
		self.world_size = (tmx_data.width * self.tilesize[0], tmx_data.height * self.tilesize[1])
		landing_zones = {} # init landing zone dict to store the landing zones for the towns
		for layer in tmx_data.visible_layers:
			# tile creation
			if isinstance(layer, pytmx.TiledTileLayer):
				for x, y, gid in layer: #type:ignore
					tile_img = tmx_data.get_tile_image_by_gid(gid)
					if not tile_img:
						continue
				
					pos = (x * TILE_SIZE[0], y * TILE_SIZE[1])

					tile = Tile(pos, tile_img, gid, layer.name) #type:ignore
				# chunking

					chunk_x = pos[0] // CHUNK_SIZE
					chunk_y = pos[1] // CHUNK_SIZE
					chunk_key = (chunk_x, chunk_y)
					self.chunked_tiles.setdefault(chunk_key, []).append(tile)
			elif isinstance(layer, pytmx.TiledObjectGroup):
				if layer.name == "player_spawn":
					for obj in layer:
						if obj.type == "spawn_point":
							if obj.name == "player_spawn":
								# set the players position
								self.player.position.update((obj.x, obj.y))
								self.camera_group.set_position(self.player.collision_rect.center)
								self.camera_group.set_zoom(1)

				elif layer.name == "landing_zones":
					for obj in layer:
						if obj.type == "landing_zone":
							landing_zones[obj.name] = pygame.Rect(obj.x, obj.y, obj.width, obj.height)


				elif layer.name == "towns":
					for obj in layer:
						if obj.type == "town":
							town_img = tmx_data.get_tile_image_by_gid(obj.gid)
							Town(town_img, (obj.x,obj.y), obj.name, layer.name, obj.properties, landing_zones, self.objects)






		# go throug each tile in chunked tiles and render it onto a surface so that each chunk is only one surface
		for chunk in self.chunked_tiles:
			surf = pygame.Surface((CHUNK_SIZE,CHUNK_SIZE), pygame.SRCALPHA)

			for tile in self.chunked_tiles[chunk]:
				x = tile.rect.left - chunk[0] * CHUNK_SIZE
				y = tile.rect.top - chunk[1] * CHUNK_SIZE
				surf.blit(tile.image, (x,y))

			tile = Tile((chunk[0] * CHUNK_SIZE, chunk[1] * CHUNK_SIZE), surf, 0, "BIG_TILES")

			self.chunked_tile_imgs[chunk] = tile




		
