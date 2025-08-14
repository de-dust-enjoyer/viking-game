from constants import *
from ship import Ship
from viking import Viking
import viking


class PlayerShip(Ship):
    def __init__(self, pos:tuple, id:str, ship_name:str, layer_name:str):
        Ship.__init__(self, pos, ship_name, id, layer_name)

        self.crew = []
        starting_crew = 4
        for i in range(starting_crew):
            viking = Viking()
            self.crew.append(viking)

        print(self.get_combat_strengt())


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


    def get_combat_strengt(self) -> tuple:
        damage = 0
        defense = 0
        for viking in self.crew:
            damage += viking.get_stat("damage")
            defense += viking.get_stat("defense")
        return damage, defense