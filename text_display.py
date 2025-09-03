from constants import *


class TextDisplay:
    def __init__(
        self,
        pos: tuple,
        img: pygame.Surface,
        font: pygame.font.Font,
        text_color: tuple,
        *lines,
    ):
        self.image = img
        self.color = text_color
        self.rect = self.image.get_rect(topleft=pos)
        self.padding = 5
        self.text_surf = pygame.Surface(
            (self.rect.width - self.padding * 2, self.rect.height - self.padding * 2),
            pygame.SRCALPHA,
        )
        self.text_surf_rect = self.text_surf.get_rect(center=(self.rect.width // 2, self.rect.height // 2))

        self.font = font
        self.font_height = self.font.render("ASDFGHJKL", False, "black").get_height()
        self.line_spacing = self.font_height + 4

        self.display_text(*lines)

    def display_text(self, *lines):
        """if a line is in all caps it will be drawn centered"""
        self.text_surf.fill((212, 165, 121))
        for index, line in enumerate(lines):
            text = self.font.render(line, False, self.color)
            if line.isupper():
                # draw_centered
                text_rect = text.get_rect(center=self.text_surf_rect.center)
            else:
                text_rect = text.get_rect(topleft=self.text_surf_rect.topleft)
            text_pos = (text_rect.left, self.line_spacing * index)
            self.text_surf.blit(text, text_pos)
        self.image.blit(self.text_surf, (self.padding, self.padding))

    def update(self, rel_mouse_pos):
        pass
