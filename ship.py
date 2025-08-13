from warnings import showwarning
from constants import *
from object import Object
from animation_player import AnimationPlayer
import ship_data

class Ship(Object):
    def __init__(self, pos:tuple, ship_name:str, id:str, layer_name:str):
        super().__init__(id,  layer_name)

        self.ship_name = ship_name

        self.animation_player = AnimationPlayer(ship_data.animations[self.ship_name], tilesize=ship_data.size[self.ship_name], starting_animation= "left_sail")
        self.image = self.animation_player.update()

        self.rect = self.image.get_frect(center = pos)
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
        self.image = self.animation_player.update()
         # flip the sprite
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



        