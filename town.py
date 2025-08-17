from constants import *
from object import Object
from soldier import Soldier

class Town(Object):
    def __init__(self, image:pygame.Surface, pos:tuple, id:str, layer_name:str, attributes:dict, landing_zones:dict, group:pygame.sprite.Group):
        Object.__init__(self, id, layer_name, group)
        self.image = image
        self.rect = self.image.get_frect(topleft= pos)
        self.attributes = attributes
        self.army = []
        for attribute in self.attributes:
            if attribute == "army_strength":
                for i in range(self.attributes[attribute]):
                    soldier = Soldier()
                    self.army.append(soldier)

        self.landing_zone = landing_zones[self.id]


    def get_combat_strengt(self) -> tuple:
        damage = 0
        defense = 0
        for soldier in self.army:
            damage += soldier.get_stat("damage")
            defense += soldier.get_stat("defense")
        return damage, defense