from constants import *
from ship import Ship
from viking import Viking
from town import Town


class PlayerShip(Ship):
    def __init__(self, pos:tuple, id:str, ship_name:str, layer_name:str, group:pygame.sprite.Group):
        Ship.__init__(self, pos, ship_name, id, layer_name, group)

        self.raid_target = None
        self.army = []
        starting_crew = 4
        for i in range(starting_crew):
            viking = Viking()
            self.army.append(viking)


    def update(self, dt):
        self.apply_player_input() # updates the velocity vector according to input
        self.move(dt) # applies the velocity vector
        self.check_if_can_raid()


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
        for viking in self.army:
            damage += viking.get_stat("damage")
            defense += viking.get_stat("defense")
        return damage, defense

    def check_if_can_raid(self):
        for obj in self.group:
            if isinstance(obj, Town):
                if self.collision_rect.colliderect(obj.landing_zone):
                    self.raid_target = obj
                else:
                    self.raid_target = None