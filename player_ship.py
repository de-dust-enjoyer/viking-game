from constants import *
from ship import Ship


class PlayerShip(Ship):
    def __init__(self, pos:tuple, id:str, ship_name:str, layer_name:str):
        Ship.__init__(self, pos, ship_name, id, layer_name)


    def update(self, dt):
        self.apply_player_input() # updates the velocity vector according to input
        self.move(dt) # applies the velocity vector


    def apply_player_input(self):
        keys = pygame.key.get_pressed()
        
        # vertical
        if keys[pygame.K_w]:
            self.velocity.y = -1
        elif keys[pygame.K_s]:
            self.velocity.y = +1

        # horizontal
        if keys[pygame.K_a]:
            self.velocity.x = -1
        elif keys[pygame.K_d]:
            self.velocity.x = +1