from constants import *
from ui_element import UiElement
from town import Town
from button import Button

class RaidMenu(UiElement):
    def __init__(self, parent, group:pygame.sprite.Group, id: str, pos: tuple, background_surf: pygame.Surface, centered=False) -> None:
        elements:dict = {
            "close_button": Button("close_button", (435, 13), "assets/sprites/ui/raid_menu/", method=self.hide),
            "scout_button": Button("scout_button", (13, 225), "assets/sprites/ui/raid_menu/"),
            "attack_button": Button("attack_button", (243, 225), "assets/sprites/ui/raid_menu/")
        }
        super().__init__(parent, group, id, pos, background_surf, centered, **elements)

        self.visible = True


        self.target = None




