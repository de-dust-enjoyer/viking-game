from constants import *
import math, random
from utils.helper_functions import get_random_point_in_area_list
from typing import Optional
from harvestable import Harvestable


class State:
    """Base state class"""

    def __init__(self, unit):
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
        self.duration = random.randint(2, 8)  # in s

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

            # Check for threats
            if distance_to_enemy < self.unit.detection_range:
                if self.unit.fight_or_flight(closest_enemy):
                    return EngagingState(closest_enemy)
                else:
                    return FleeingState(closest_enemy)

        # find the nearest item if there is any
        if items:
            closest_item = min(items, key=lambda item: self.unit.distance_to(item.rect.centerx, item.rect.centery))
            distance_to_item = self.unit.distance_to(closest_item.rect.centerx, closest_item.rect.centery)

            # check if there is a item in vicinity
            if distance_to_item < self.unit.detection_range:
                return CollectingState(self.unit, closest_item)

        # Random transitions
        if self.timer > self.duration:
            choice = random.random()
            if choice < 0.6:
                return RoamingState(self.unit)
            elif choice < 0.8 and harvestables:
                nearest = min(harvestables, key=lambda r: self.unit.distance_to(r.rect.centerx, r.rect.centery))
                if self.unit.distance_to(nearest.rect.centerx, nearest.rect.centery) < 500:
                    return HarvestingState(self.unit, nearest)

        return None


class RoamingState(State):
    def enter(self):
        super().enter()
        self.duration = 10  # in s: fallback for when the unit cannot reach its target

        if self.unit.roaming_space is not None:
            self.target = get_random_point_in_area_list(self.unit.roaming_space)
        else:
            roam_range = 200  # how many pixels in each direction the unit is allowed to roam
            random_x = random.randrange(int(self.unit.rect.centerx - roam_range), int(self.unit.rect.centerx + roam_range))
            random_y = random.randrange(int(self.unit.rect.centery - roam_range), int(self.unit.rect.centery + roam_range))
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

            # Check for threats
            if distance_to_enemy < self.unit.detection_range:
                if self.unit.fight_or_flight(closest_enemy):
                    return EngagingState(self.unit, closest_enemy)
                else:
                    return FleeingState(self.unit, closest_enemy)

        reached = self.unit.move_to_point(self.target[0], self.target[1])

        # find the nearest item if there is any
        if items:
            closest_item = min(items, key=lambda item: self.unit.distance_to(item.rect.centerx, item.rect.centery))
            distance_to_item = self.unit.distance_to(closest_item.rect.centerx, closest_item.rect.centery)

            # check if there is a item in vicinity
            if distance_to_item < self.unit.detection_range:
                return CollectingState(self.unit, closest_item)

        if reached or self.timer >= self.duration:
            return IdleState(self.unit)

        return None


class HarvestingState(State):
    def __init__(self, unit, harvestable: Harvestable):
        super().__init__(unit)
        self.target = harvestable

    def enter(self):
        super().enter()
        self.duration = 30

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

            # Check for threats
            if distance_to_enemy < self.unit.detection_range:
                if self.unit.fight_or_flight(closest_enemy):
                    return EngagingState(closest_enemy)
                else:
                    return FleeingState(closest_enemy)

        reached = self.unit.move_to_point(self.target.rect.centerx, self.target.rect.centery)
        if reached:
            self.unit.harvest(self.target)

        if self.target.state == "depleted" or self.timer >= self.duration:
            return IdleState(self.unit)

        return None


class CollectingState(State):
    def __init__(self, unit, item):
        super().__init__(unit)
        self.target = item

    def enter(self):
        super().enter()
        self.duration = 10

    def update(self, units, harvestables, items, dt):
        super().update(units, harvestables, items, dt)
        if self.target not in items:
            return IdleState(self.unit)

        enemy_units = []
        for unit in units:
            # if the unit is from another faction
            if unit.allegiance != self.unit.allegiance and not unit.dead:
                enemy_units.append(unit)
        if enemy_units:
            closest_enemy = min(enemy_units, key=lambda unit: self.unit.distance_to(unit.x, unit.y))
            distance_to_enemy = self.unit.distance_to(closest_enemy.rect.centerx, closest_enemy.rect.centery)

            # Check for threats
            if distance_to_enemy < self.unit.detection_range:
                if self.unit.fight_or_flight(closest_enemy):
                    return EngagingState(closest_enemy)
                else:
                    return FleeingState(closest_enemy)

        reached = self.unit.move_to_point(self.target.rect.centerx, self.target.rect.centery, 1)
        if reached:
            self.unit.pick_up_item(self.target)
            return IdleState(self.unit)
