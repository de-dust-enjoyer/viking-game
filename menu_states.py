from constants import *
from utils.game_state_manager import GameStateManager


class before_raid:
    def __init__(self, menu_state_manager: GameStateManager):
        self.menu_state_manager = menu_state_manager

    def run(self, dt: float, events) -> None:
        pass


class after_raid:
    def __init__(self, menu_state_manager: GameStateManager):
        self.menu_state_manager = menu_state_manager

    def run(self, dt: float, events) -> None:
        pass


class ingame_menu:
    def __init__(self, menu_state_manager: GameStateManager):
        self.menu_state_manager = menu_state_manager

    def run(self, dt: float, events) -> None:
        pass
