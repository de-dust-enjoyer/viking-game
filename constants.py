import pygame, sys
from os.path import join

# constants
SCREEN_SIZE = (960, 540)
GAME_TITLE = "Viking Game"
STARTING_STATE = "world"

TILE_SIZE = (16, 16)

INVENTORY_GRID_SIZE = 34

# chunking
CHUNK_SIZE = 128
RENDER_DIST = (4, 3)  # x, y in chunks


NO_COLOR = (1, 1, 1)
