from constants import *
from base_classes.object import Object
from pygame_animation_player import Animation, AnimationPlayer
from typing import Optional
import data.ship_data as ship_data

class Ship(Object):
    def __init__(self, pos:tuple, ship_name:str, id:str, layer_name:str, group:pygame.sprite.Group):
        super().__init__(id,  layer_name, group)

        self.ship_name = ship_name

        self.image:Optional[pygame.Surface] = None
        horizontal = Animation(0, pygame.image.load(join("assets", "sprites", "ships", "viking_ship_01", "left_sail.png")).convert_alpha())
        up = Animation(0, pygame.image.load(join("assets", "sprites", "ships", "viking_ship_01", "up_sail.png")).convert_alpha())
        down = Animation(0, pygame.image.load(join("assets", "sprites", "ships", "viking_ship_01", "down_sail.png")).convert_alpha())
        self.animation_player = AnimationPlayer(self, horizontal=horizontal, up=up, down=down)
        self.animation:str = "horizontal"


        self.rect = self.image.get_frect(center = pos) # type:ignore
        self.collision_rect = pygame.Rect(self.rect.center ,ship_data.collision_size[self.ship_name])

        # movement
        self.velocity = pygame.Vector2(0,0)
        self.position = pygame.Vector2(pos)

        self.speed = ship_data.speed[self.ship_name]
        

    def update(self, dt):
        self.move(dt)






    def move(self, dt):
        # normalize the vector if len > 1
        if self.velocity.length() > 1:
            self.velocity = self.velocity.normalize()

        # update animations according to velocity
        if self.velocity.y > abs(self.velocity.x):
            # ship going down
            self.animation_player.play("down")
        elif self.velocity.y < -abs(self.velocity.x):
            # ship going up
            self.animation_player.play("up")
        elif self.velocity.length() != 0:
            # ship going horizontal
            self.animation_player.play("horizontal")

        
        self.animation_player.update(dt)
        
        if self.velocity.x > 0:
            self.flip_h = True
        elif self.velocity.x < 0:
            self.flip_h = False
        #else keep flip_h


        # apply velocity vector with speed and dt
        self.position += self.velocity * self.speed * dt
        # apply position to rect and collision rect
        self.collision_rect.center = self.position
        self.rect.center = self.collision_rect.center

        # reset velocity vector
        self.velocity.x = 0; self.velocity.y = 0



        