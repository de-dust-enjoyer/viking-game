from constants import *
from base_classes.object import Object


class Harvestable(Object):
    def __init__(self, pos, type, layer_name, group):
        super().__init__(type, layer_name, group)

        self.state = "rich"

        self.health = 100

        self.imgs = {
            "rich": pygame.image.load(join("assets", "sprites", "world", "harvestables", type, "rich.png")).convert_alpha(),
            "depleted": pygame.image.load(join("assets", "sprites", "world", "harvestables", type, "depleted.png")).convert_alpha(),
        }
        self.image = self.imgs[self.state]
        self.rect = self.image.get_rect(topleft=pos)

    def get_hurt(self, damage: float):
        if self.state == "rich":
            self.health -= damage
            if self.health <= 0:
                self.state = "depleted"

    def update(self, dt):
        self.image = self.imgs[self.state]
