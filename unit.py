from constants import *
from states import State, IdleState, RoamingState, CollectingState, HarvestingState
from typing import Dict
from base_classes.person import Person
from pygame_animation_player import AnimationPlayer, Animation
from data.unit_appearance import get_random_appearance
from utils.timer import Timer
import random, math


class Unit(Person):
    def __init__(self, type: str, allegiance: str, starting_pos: tuple, group: pygame.sprite.Group, roaming_space: list, name=None, attr=None):
        """name format = (forename, surname), attribute format = {category: {attribute: {stat: value}}}"""
        super().__init__(type, name, attr)
        group.add(self)
        self.image = None
        self.dead = False
        self.detection_range = 30
        self.allegiance = allegiance
        self.tile_size = (64, 64)
        self.animation_fps = 10
        self.movement_speed = 20
        self.direction = pygame.Vector2(0, 0)
        self.inventory = []

        self.harvest_timer = Timer(1.0, False)

        self.roaming_space = roaming_space

        self.current_state = IdleState(self)
        self.current_state.enter()

        self.appearance = get_random_appearance(allegiance)

        animations = self.get_animations()

        self.animation_player = AnimationPlayer(self, **animations)
        self.animation_player.play("idle_down")
        self.rect = self.image.get_frect(topleft=starting_pos)

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

    def move(self, dt):
        if self.direction.length() > 1:
            self.direction = self.direction.normalize()
        self.rect.topleft += self.direction * self.movement_speed * dt

    def change_state(self, new_state):
        """Transition to a new state"""
        if new_state:
            self.current_state.exit()
            self.current_state = new_state
            self.current_state.enter()

    def get_state_name(self):
        return self.current_state.__class__.__name__.replace("State", "").lower()

    def update(self, units, harvestables, items, dt):
        # Update current state and check for transitions
        new_state = self.current_state.update(units, harvestables, items, dt)
        if new_state:
            self.change_state(new_state)
        self.move(dt)
        self.animation_player.update(dt)

    def scale_by(self, scale: float):
        return pygame.transform.scale_by(self.image, scale)

    def distance_to(self, x: float, y: float):
        return math.sqrt(abs(self.rect.centerx - x + self.rect.centery - y))

    def move_to_point(self, x, y, tolerance=10):
        dx = x - self.rect.centerx
        dy = y - self.rect.centery
        self.direction.update(dx, dy)
        if abs(dx) <= tolerance and abs(dy) <= tolerance:
            return True

        return False

    def fight_or_flight(self, enemy_unit: "Unit"):
        if random.choice([0, 1]):
            return True
        else:
            return False

    def pick_up_item(self, item: pygame.sprite.Sprite):
        self.inventory.append(item)
        item.kill()

    def harvest(self, harvestable):
        if not self.harvest_timer.is_running():
            self.harvest_timer.start()
        if self.harvest_timer.update():
            harvestable.get_hurt(self.damage)
