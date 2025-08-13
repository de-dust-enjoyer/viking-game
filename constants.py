import pygame, sys
from os.path import join

# constants
SCREEN_SIZE = (960 * 2, 540 * 2)
GAME_TITLE = "Viking Game"
STARTING_STATE = "world"

TILE_SIZE = (16, 16) 

# chunking
CHUNK_SIZE = 64
RENDER_DIST = (8,5) # x, y in chunks