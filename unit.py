from constants import *
from typing import Dict
from base_classes.person import Person
from pygame_animation_player import AnimationPlayer, Animation
from data.unit_appearance import get_random_appearance
import random


class Unit(Person):
    def __init__(self, type: str, allegiance: str, starting_pos: tuple, group: pygame.sprite.Group, name=None, attr=None):
        """name format = (forename, surname), attribute format = {category: {attribute: {stat: value}}}"""
        super().__init__(type, name, attr)
        group.add(self)
        self.print_info()
        self.image = None
        self.dead = False
        self.allegiance = allegiance
        self.tile_size = (64, 64)
        self.animation_fps = 10
        self.movement_speed = 10

        self.appearance = get_random_appearance(allegiance)

        animations = self.get_animations()

        self.animation_player = AnimationPlayer(self, **animations)
        self.animation_player.play("idle_down")
        self.rect = self.image.get_rect(topleft=starting_pos)
        print(self.rect)

    def get_animations(self) -> dict:
        image_dict = {}
        animation_dict = {}
        render_order = ["feet", "legs", "chest", "head", "accessories", "hands"]
        animations = [
            "idle_down",
            "idle_side",
            "idle_up",
            "walk_down",
            "walk_side",
            "walk_up",
            "die",
            "hit_down",
            "hit_side",
            "hit_up",
            "attack_0_down",
            "attack_1_down",
            "attack_2_down",
            "attack_0_side",
            "attack_1_side",
            "attack_2_side",
            "attack_0_up",
            "attack_1_up",
            "attack_2_up",
        ]
        for animation in animations:
            image_dict[animation] = pygame.image.load(join("assets", "sprites", "units", "base", self.appearance["base"], animation + ".png")).convert_alpha()
            for component in render_order:
                image_dict[animation].blit(pygame.image.load(join("assets", "sprites", "units", component, self.appearance[component], animation + ".png")).convert_alpha())
            animation_dict[animation] = Animation(self.animation_fps, image_dict[animation], tilesize=self.tile_size)
        return animation_dict

    def update(self, dt):
        self.animation_player.update(dt)

    def scale_by(self, scale: float):
        return pygame.transform.scale_by(self.image, scale)
