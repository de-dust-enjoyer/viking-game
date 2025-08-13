import pygame, sys
from os.path import join

# constants
SCREEN_SIZE = (960 * 2, 540 * 2)
GAME_TITLE = "Viking Game"
STARTING_STATE = "world"

TILE_SIZE = (16, 16) 

# chunking
CHUNK_SIZE = 256
RENDER_DIST = (3,2) # x, y in chunks