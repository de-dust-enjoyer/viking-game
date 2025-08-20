import pygame


def render_text_with_outline(
    text: str,
    text_font: pygame.Font,
    text_color: tuple = (255, 255, 255),
    outline_color: tuple = (0, 0, 0),
    outline_width: int = 2,
) -> pygame.Surface:
    """outline font should be a little big bigger then text font"""

    text_surf = text_font.render(text, False, text_color)
    outline_surf = pygame.transform.scale(
        text_font.render(text, False, outline_color),
        (text_surf.get_width() + outline_width, text_surf.get_height() + outline_width),
    )
    outline_rect = outline_surf.get_rect(topleft=(0, 0))
    surf = pygame.Surface(outline_surf.get_size(), pygame.SRCALPHA)
    text_rect = text_surf.get_rect(center=outline_rect.center)
    surf.blit(outline_surf, (0, 0))
    surf.blit(text_surf, text_rect)
    return surf


def text_outline(font, message, fontcolor, outlinecolor):
    base = font.render(message, 0, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), 16)
    img.blit(base, (1, 1))
    img.blit(outline, (0, 0))
    img.set_colorkey(0)
    return img


def textHollow(font, message, fontcolor):
    notcolor = [c ^ 0xFF for c in fontcolor]
    base = font.render(message, 0, fontcolor, notcolor)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, 16)
    img.fill(notcolor)
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img
