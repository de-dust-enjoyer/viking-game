from constants import *
from base_classes.ui_element import UiElement
from typing import Optional

class ButtonPrompt(UiElement):
    def __init__(self, parent, group:pygame.sprite.Group, text:str, key:int, font:pygame.Font):
        space_name_img = 10
        text_color = (200,200,200)
        
        text_surf = font.render(text, False, text_color)
        og_img_surf = pygame.image.load(join("assets", "sprites", "ui", "key_tiles", str(key)+".png")).convert_alpha()
        img_surf = pygame.transform.scale_by(og_img_surf, 2)

        surf_w = text_surf.get_width() + img_surf.get_width() + space_name_img
        surf_h = max(text_surf.get_height(), img_surf.get_height())
        
        img_pos_x = 0
        img_pos_y = surf_h // 2 - img_surf.get_height() // 2

        text_pos_x = img_pos_x + img_surf.get_width() + space_name_img
        text_pos_y = surf_h // 2 - text_surf.get_height() // 2

        surf = pygame.Surface((surf_w, surf_h), pygame.SRCALPHA)
        surf.blit(img_surf, (img_pos_x, img_pos_y))
        surf.blit(text_surf, (text_pos_x, text_pos_y))

        pos = parent.parent.screen.get_width() // 2, parent.parent.screen.get_height() // 2 + 100

        UiElement.__init__(self, parent, group, "button_prompt "+text+" "+str(key), pos, surf, centered=True)

        self.key = key

    def update(self, dt):
        self.visible = False
        if self.parent.parent.player.raid_target and not self.parent.visible:
            self.visible = True
            if pygame.key.get_pressed()[self.key]:
                self.parent.visible = True
                