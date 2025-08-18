from constants import *
from base_classes.ui_element import UiElement
from typing import Optional

class ButtonPrompt(UiElement):
    def __init__(self, parent, group:pygame.sprite.Group, text:str, key:int, key_images:pygame.Surface, font:pygame.Font)
        space_name_img = 10
        text_color = (200,200,200)
        text_surf = font.render(text, False, text_color)
        img_surf = 

        UiElement.__init__(self, parent, group, "button_prompt "+text+" "+key, pos, surf, centered=True)
