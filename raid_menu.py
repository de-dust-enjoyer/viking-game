from constants import *
from base_classes.ui_element import UiElement
from town import Town
from button import Button
from typing import Optional
from button_prompt import ButtonPrompt

class RaidMenu(UiElement):
    def __init__(self, parent, group:pygame.sprite.Group, id: str, pos: tuple, background_surf: pygame.Surface, centered=False) -> None:
        elements:dict = {
            "close_button": Button("close_button", (435, 13), "assets/sprites/ui/raid_menu/", method=self.hide),
            "scout_button": Button("scout_button", (13, 225), "assets/sprites/ui/raid_menu/"),
            "attack_button": Button("attack_button", (243, 225), "assets/sprites/ui/raid_menu/")
        }
        super().__init__(parent, group, id, pos, background_surf, centered, **elements)

        self.visible = False
        self.parent = parent
        self.town:Optional[Town] = self.parent.player.raid_target

        self.button_prompt = ButtonPrompt(self, self.group, "investigate", pygame.K_f, pygame.font.Font("assets/font/Norse-Bold.otf", 25))


    def update(self, dt):
        if not self.parent.player.raid_target:
            self.visible = False
            self.parent.camera_group.remove_target()
        else:
            self.parent.camera_group.set_target(self.parent.player.raid_target)
    

        self.update_components()




