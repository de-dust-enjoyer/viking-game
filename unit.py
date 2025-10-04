from constants import *
from base_classes.person import Person
from pygame_animation_player import AnimationPlayer, Animation


class Unit(Person):
    def __init__(self, type: str, allegiance: str, starting_pos: tuple, group: pygame.sprite.Group, name=None, attr=None):
        """name format = (forename, surname), attribute format = {category: {attribute: {stat: value}}}"""
        super().__init__(type, name, attr)
        group.add(self)
        self.print_info()
        self.image = None
        self.dead = False
        self.allegiance = allegiance
        self.movement_speed = 10

        self.appearance = {"base": "base"}

        animations_base = {
            "idle_down": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "idle_down.png")).convert_alpha(), tilesize=(64, 64)),
            "idle_side": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "idle_side.png")).convert_alpha(), tilesize=(64, 64)),
            "idle_up": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "idle_up.png")).convert_alpha(), tilesize=(64, 64)),
            "walk_down": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "walk_down.png")).convert_alpha(), tilesize=(64, 64)),
            "walk_side": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "walk_side.png")).convert_alpha(), tilesize=(64, 64)),
            "walk_up": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "walk_up.png")).convert_alpha(), tilesize=(64, 64)),
            "die": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "die.png")).convert_alpha(), tilesize=(64, 64)),
            "hit_down": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "hit_down.png")).convert_alpha(), tilesize=(64, 64)),
            "hit_side": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "hit_side.png")).convert_alpha(), tilesize=(64, 64)),
            "hit_up": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "hit_up.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_0_down": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_0_down.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_1_down": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_1_down.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_2_down": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_2_down.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_0_side": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_0_side.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_1_side": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_1_side.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_2_side": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_2_side.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_0_up": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_0_up.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_1_up": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_1_up.png")).convert_alpha(), tilesize=(64, 64)),
            "attack_2_up": Animation(10, pygame.image.load(join("assets", "sprites", "units", self.appearance["base"], "attack_2_up.png")).convert_alpha(), tilesize=(64, 64)),
        }
        self.animation_player = AnimationPlayer(self, **animations_base)
        self.animation_player.play("idle_down ")
        self.rect = self.image.get_rect(topleft=starting_pos)
        print(self.rect)

    def update(self, dt):
        self.animation_player.update(dt)

    def scale_by(self, scale: float):
        return pygame.transform.scale_by(self.image, scale)
