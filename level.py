from constants import *
import pytmx
from base_classes.ship import Ship
from building import Building
from camera import CameraGroup
from town import Town
from base_classes.tile import Tile, AnimatedTile, TileAnimationManager
from grid_inventory import GridInventory
from ui_group import UiGroup
from utils.helper_functions import get_random_point_in_area_list
from harvestable import Harvestable
from unit import Unit
import random


class Level:
    def __init__(self, screen: pygame.Surface, game_state_manager, game):
        self.screen = screen
        self.game_state_manager = game_state_manager
        self.game = game

        self.town = None

        self.npc_roaming_space = []  # list of areas the npcs are allowed to move
        # = [rect, rect, rect]

        # chunking
        self.chunked_tiles = {}  # {(chunk_x, chunk_y): [Tile, Tile, Tile ...]} # for collisions
        self.chunked_animated_tiles = {}  # {(chunk_x, chunk_y): [Tile, Tile, Tile ...]} # for rendering animated tiles
        self.chunked_tile_imgs = {}  # {(chunk_x, chunk_y): BIG_TILE} # for rendering

        # can only chunk static objects
        self.chunked_static_objects = {}  # {(chunk_x, chunk_y): [Object, Object, ...]}

        self.tilesize = TILE_SIZE
        self.level_size = (0, 0)

        # groups
        self.dynamic_objects = pygame.sprite.Group()
        self.animated_tiles = pygame.sprite.Group()
        self.static_objects = pygame.sprite.Group()

        self.units = pygame.sprite.Group()
        self.harvestables = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.buildings = pygame.sprite.Group()

        self.camera_group = CameraGroup(self.screen, [self.dynamic_objects], self.chunked_tile_imgs, self.chunked_static_objects, self.chunked_animated_tiles, CHUNK_SIZE, type="mouse")
        self.ui_group = UiGroup()

        self.tile_animation_manager = TileAnimationManager()
        self.has_level = False

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def run(self, dt: float, events):
        if self.town is not None:
            if not self.has_level:
                self.has_level = self.build_level(self.town)

        # input

        # logic

        for building in self.buildings:
            building.update(dt)
        for item in self.items:
            item.update(dt)
        for harvestable in self.harvestables:
            harvestable.update(dt)
        for unit in self.units:
            unit.update(self.units.sprites(), self.harvestables.sprites(), self.items.sprites(), dt)

        self.tile_animation_manager.update()

        self.ui_group.update(dt, events)

        # rendering
        self.camera_group.custom_draw(dt)
        self.ui_group.draw(self.screen)

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def build_level(self, town: Town):
        town_name = town.id
        if self.town is None:
            return False
        self.screen.blit(
            pygame.image.load(join("assets", "sprites", "ui", "loading_screen", "loading_screen.png")).convert_alpha(),
            (0, 0),
        )
        pygame.display.flip()
        tmx_data = pytmx.util_pygame.load_pygame(join("assets", "tiled", "towns", town_name + ".tmx"))  # type:ignore
        self.tilesize = (tmx_data.tilewidth, tmx_data.tileheight)
        self.level_size = (
            tmx_data.width * self.tilesize[0],
            tmx_data.height * self.tilesize[1],
        )
        for layer in tmx_data.visible_layers:
            # tile creation

            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:  # type:ignore
                    frames = []
                    frame_duration = 0
                    tile_pos = (x * TILE_SIZE[0], y * TILE_SIZE[1])
                    # chunking
                    # calculate which chunk the tile is in
                    chunk_x = tile_pos[0] // CHUNK_SIZE
                    chunk_y = tile_pos[1] // CHUNK_SIZE

                    chunk_key = (chunk_x, chunk_y)
                    # get the tile propertys (for animation)
                    tile_props = tmx_data.get_tile_properties_by_gid(gid)
                    # check if the tile has properties
                    if tile_props:
                        # check if the tile has animation frames
                        if tile_props["frames"] and len(tile_props["frames"]) > 1:
                            # check if there are any frames in frames
                            # create empty list to append the animaiton frames
                            for frame in tile_props["frames"]:
                                frame_img = tmx_data.get_tile_image_by_gid(frame.gid)
                                frame_duration = frame.duration
                                frames.append(frame_img)
                            # create animated tile
                            tile = AnimatedTile(tile_pos, frames, frame_duration, gid, layer.name)  # type:ignore
                            # chunk da shiiiit outa this tile
                            self.chunked_animated_tiles.setdefault(chunk_key, []).append(tile)

                    # if the tile does not have properties create a normal tile
                    else:
                        tile_img = tmx_data.get_tile_image_by_gid(gid)
                        if not tile_img:
                            continue
                        # create tile
                        tile = Tile(tile_pos, tile_img, gid, layer.name)  # type:ignore
                        # place tile in the coresponding chunk (chunk dat shiiiit)
                        self.chunked_tiles.setdefault(chunk_key, []).append(tile)

            elif isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == "ships":
                    for obj in layer:
                        if obj.type == "ship":
                            ship_img = tmx_data.get_tile_image_by_gid(obj.gid)
                            ship = Ship((obj.x, obj.y), "viking_ship_01", obj.name, layer.name, self.dynamic_objects)
                            self.camera_group.set_position((obj.x, obj.y))

                elif layer.name == "houses":
                    for obj in layer:
                        house_img = tmx_data.get_tile_image_by_gid(obj.gid)
                        house = Building(house_img, (obj.x, obj.y), obj.name, layer.name, self.dynamic_objects)
                        for i in range(random.randint(1, 2)):
                            villager = Unit("english", "civilian", get_random_point_in_area_list(self.npc_roaming_space), self.dynamic_objects, self.npc_roaming_space)
                            self.units.add(villager)

                elif layer.name == "npc_roaming_space":
                    for obj in layer:
                        self.npc_roaming_space.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

                elif layer.name == "harvestables":
                    for obj in layer:
                        harvestable = Harvestable((obj.x, obj.y), obj.type, layer.name, self.dynamic_objects, self.items)
                        self.harvestables.add(harvestable)

        # go throug each tile in chunked tiles and render it onto a surface so that each chunk is only one surface
        for chunk in self.chunked_tiles:
            surf = pygame.Surface((CHUNK_SIZE, CHUNK_SIZE), pygame.SRCALPHA)

            for tile in self.chunked_tiles[chunk]:
                x = tile.rect.left - chunk[0] * CHUNK_SIZE
                y = tile.rect.top - chunk[1] * CHUNK_SIZE
                surf.blit(tile.image, (x, y))

            tile = Tile((chunk[0] * CHUNK_SIZE, chunk[1] * CHUNK_SIZE), surf, 0, "BIG_TILES")

            self.chunked_tile_imgs[chunk] = tile

        # init the animation manager with the animation tiles
        self.tile_animation_manager.init(self.chunked_animated_tiles)

        return True
