from constants import *

size = {
    "viking_ship_01": (138,138)
}
collision_size = {
    "viking_ship_01": (128,128)
} 
speed = {
    "viking_ship_01": 100
}
animations = {
    "viking_ship_01": {
        "left_sail": pygame.image.load(join("assets", "sprites", "ships", "viking_ship_01", "left_sail.png")),
        "right_sail": pygame.image.load(join("assets", "sprites", "ships", "viking_ship_01", "left_sail.png")),
        "up_sail": pygame.image.load(join("assets", "sprites", "ships", "viking_ship_01", "left_sail.png")),
        "down_sail": pygame.image.load(join("assets", "sprites", "ships", "viking_ship_01", "left_sail.png"))
    }
}