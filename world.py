from constants import *
from camera import CameraGroup
from ui_group import UiGroup
from player_ship import PlayerShip
from base_classes.tile import Tile, AnimatedTile, TileAnimationManager
from town import Town
from raid_menu import RaidMenu
from inventory import Inventory

import pytmx


class World:
    def __init__(self, screen, game_state_manager, game):
        self.screen = screen
        self.game_state_manager = game_state_manager
        self.game = game

        # chunking
        self.chunked_tiles = {}  # {(chunk_x, chunk_y): [Tile, Tile, Tile ...]} # for collisions
        self.chunked_animated_tiles = {}  # {(chunk_x, chunk_y): [Tile, Tile, Tile ...]} # for rendering animated tiles
        self.chunked_tile_imgs = {}  # {(chunk_x, chunk_y): BIG_TILE} # for rendering

        # can only chunk static objects
        self.chunked_static_objects = {}  # {(chunk_x, chunk_y): [Object, Object, ...]}

        self.world_size = (0, 0)
        self.tilesize = (0, 0)

        # groups
        self.dynamic_objects = pygame.sprite.Group()
        self.animated_tiles = pygame.sprite.Group()
        self.static_objects = pygame.sprite.Group()
        self.camera_group = CameraGroup(
            self.screen,
            [self.dynamic_objects],
            self.chunked_tile_imgs,
            self.chunked_static_objects,
            self.chunked_animated_tiles,
            CHUNK_SIZE,
        )
        self.ui_group = UiGroup()

        self.tile_animation_manager = TileAnimationManager()

        self.player = PlayerShip(self, "viking_ship_01", self.dynamic_objects)
        self.camera_group.set_target(self.player, permanent=True)

        self.build_world()

        # ui elements:

        self.raid_menu = RaidMenu(
            self,
            self.ui_group,
            "raid_menu",
            (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2 - 100),
            pygame.image.load("assets/sprites/ui/raid_menu/background_surface.png").convert_alpha(),
            centered=True,
        )

        self.inventory_menu = Inventory(self, self.ui_group)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def run(self, dt: float, events):
        # input

        # logic
        for obj in self.dynamic_objects:
            obj.update(dt)

        self.tile_animation_manager.update()

        self.ui_group.update(dt, events)

        # rendering
        self.camera_group.custom_draw(dt)
        self.ui_group.draw(self.screen)

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def build_world(self):
        self.screen.blit(
            pygame.image.load(join("assets", "sprites", "ui", "loading_screen", "loading_screen.png")).convert_alpha(),
            (0, 0),
        )
        pygame.display.flip()
        tmx_data = pytmx.util_pygame.load_pygame(join("assets", "tiled", "levels", "test_world_02.tmx"))  # type:ignore
        self.tilesize = (tmx_data.tilewidth, tmx_data.tileheight)
        self.world_size = (
            tmx_data.width * self.tilesize[0],
            tmx_data.height * self.tilesize[1],
        )
        landing_zones = {}  # init landing zone dict to store the landing zones for the towns
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
                            town = Town(
                                town_img,
                                (obj.x, obj.y),
                                obj.name,
                                layer.name,
                                obj.properties,
                                landing_zones,
                                self.static_objects,
                            )

                            # chunk it
                            chunk_x = obj.x // CHUNK_SIZE
                            chunk_y = obj.y // CHUNK_SIZE

                            chunk_key = (chunk_x, chunk_y)

                            self.chunked_static_objects.setdefault(chunk_key, []).append(town)

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
