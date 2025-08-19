from constants import *
from base_classes.ship import Ship
from viking import Viking
from town import Town
from utils.chunking import get_nearby_static_objects
import random


class PlayerShip(Ship):
    def __init__(self, parent, ship_name:str, group:pygame.sprite.Group):
        Ship.__init__(self, (0, 0), ship_name, "player", "ships", group)
        self.parent = parent
        self.raid_target = None
        self.army = []
        starting_crew = 4
        for i in range(starting_crew):
            viking = Viking()
            self.army.append(viking)

        self.known_towns:dict = {} # {town_name: {name:öalkdfakl, army_strenght: salfjaöls, ....}


    def update(self, dt):
        self._apply_player_input() # updates the velocity vector according to input
        self.move(dt) # applies the velocity vector
        self._check_if_can_raid()


    def _apply_player_input(self):
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

    def _check_if_can_raid(self) -> None:
        
        range_x, range_y = 5, 4 # how big of an area is to be checked in chunks
        nearby_static_objects = get_nearby_static_objects(self.collision_rect.center, self.parent.chunked_static_objects, CHUNK_SIZE, range_x, range_y) # type:ignore
        for object in nearby_static_objects:
            if isinstance(object, Town):
                if self.collision_rect.colliderect(object.landing_zone):
                    self.raid_target = object
                    return
        self.raid_target = None

    def scout(self):
        print("suii")
        if not self.raid_target.id in self.known_towns:
            self.known_towns[self.raid_target.id] = {}

        self.known_towns[self.raid_target.id]["name"] = self.raid_target.id
        self.known_towns[self.raid_target.id]["army_size"] = len(self.raid_target.army)
        self.known_towns[self.raid_target.id]["loot_value"] = self.raid_target.loot_value
        print(self.known_towns)
