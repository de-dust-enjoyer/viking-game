from constants import *
import math, random
from unit import Unit
from utils.helper_functions import get_random_point_in_area_list
from typing import Optional


class State:
    """Base state class"""

    def __init__(self, unit: Unit):
        self.unit = unit
        self.timer: float = 0

    def enter(self):
        """Called when entering this state"""
        self.timer = 0

    def update(self, units, harvestables, items, dt) -> Optional["State"]:
        """Update logic returns new state if transition occurs"""
        self.timer += dt
        return None

    def exit(self):
        """Called when exiting this state"""
        pass


class IdleState(State):
    def enter(self):
        super().enter()
        self.duration = random.randint(60, 180)  # in ms

    def update(self, units, harvestables, items, dt):
        super().update(units, harvestables, items, dt)

        enemy_units = []
        for unit in units:
            # if the unit is from another faction
            if unit.allegiance != self.unit.allegiance and not unit.dead:
                enemy_units.append(unit)
        if enemy_units:
            closest_enemy = min(enemy_units, key=lambda unit: self.unit.distance_to(unit.x, unit.y))
            distance_to_enemy = self.unit.distance_to(closest_enemy.rect.centerx, closest_enemy.rect.centery)
        else:
            # if no enemy unit exists (this will never happen)
            closest_enemy = None
            distance_to_enemy = None

        # Check for threats
        if distance_to_enemy < self.unit.detection_range:
            if self.unit.fight_or_flight(closest_enemy):
                return EngagingState(closest_enemy)
            else:
                return FleeingState(closest_enemy)

        # Random transitions
        if self.timer > self.duration:
            choice = random.random()
            if choice < 0.6:
                return RoamingState(self.unit)
            elif choice < 0.8 and harvestables:
                nearest = min(harvestables, key=lambda r: self.unit.distance_to(r.rect.centerx, r.rect.centery))
                if self.unit.distance_to(nearest.rect.centerx, nearest.rect.centery) < 500:
                    return HarvestingState(self.unit, nearest.rect.centerx, nearest.rect.centery)

        return None


class RoamingState(State):
    def enter(self):
        super().enter()
        self.duration = 10000  # in ms: fallback for when the unit cannot reach its target

        if self.unit.roaming_space is not None:
            self.target = get_random_point_in_area_list(self.unit.roaming_space)
        else:
            roam_range = 200  # how many pixels in each direction the unit is allowed to roam
            random_x = random.randrange(int(self.unit.rect.centerx - roam_range), int(self.unit.rect.centerx - roam_range))
            random_y = random.randrange(int(self.unit.rect.centery - roam_range), int(self.unit.rect.centery - roam_range))
            self.target = random_x, random_y

    def update(self, units, harvestables, items, dt):
        super().update(units, harvestables, items, dt)

        enemy_units = []
        for unit in units:
            # if the unit is from another faction
            if unit.allegiance != self.unit.allegiance and not unit.dead:
                enemy_units.append(unit)
        if enemy_units:
            closest_enemy = min(enemy_units, key=lambda unit: self.unit.distance_to(unit.x, unit.y))
            distance_to_enemy = self.unit.distance_to(closest_enemy.rect.centerx, closest_enemy.rect.centery)
        else:
            # if no enemy unit exists (this will never happen)
            closest_enemy = None
            distance_to_enemy = None

        # Check for threats
        if distance_to_enemy < self.unit.detection_range:
            if self.unit.fight_or_flight(closest_enemy):
                return EngagingState(closest_enemy)
            else:
                return FleeingState(closest_enemy)

        reached = self.unit.move_to_point(self.target[0], self.target[1])

        if reached or self.timer >= self.duration:
            return IdleState(self.unit)

        return None


class HarvestingState(State):
    def enter(self, target_x, target_y):
        super().enter()
        self.duration = 20000
        self.target = target_x, target_y

    def update(self, units, harvestables, items, dt):
        super().update(units, harvestables, items, dt)
        enemy_units = []
        for unit in units:
            # if the unit is from another faction
            if unit.allegiance != self.unit.allegiance and not unit.dead:
                enemy_units.append(unit)
        if enemy_units:
            closest_enemy = min(enemy_units, key=lambda unit: self.unit.distance_to(unit.x, unit.y))
            distance_to_enemy = self.unit.distance_to(closest_enemy.rect.centerx, closest_enemy.rect.centery)
        else:
            # if no enemy unit exists (this will never happen)
            closest_enemy = None
            distance_to_enemy = None

        reached = self.unit.move_to_point(self.target[0], self.target[1])
        if reached()