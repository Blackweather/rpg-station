import pygame
from . import window

class ControlPrompt(window.Window):
    def __init__(self, screen, control_to_change):
        self.screen = screen
        self.control_to_change = control_to_change
        self.PROMPT_TEXT = "Press any button to set the control..."

        super().init_pygame()

    def get_font_size(self):
        TESTED_RESOLUTION = 1920 * 1080
        DEFAULT_FONTS = (100, 100)

        w, h = pygame.display.get_surface().get_size()
        current_resolution = w * h
        if current_resolution == TESTED_RESOLUTION:
            return DEFAULT_FONTS

        # else calculate the fonts
        title_font = int((current_resolution / TESTED_RESOLUTION) * DEFAULT_FONTS[0])
        opt_font = int((current_resolution / TESTED_RESOLUTION) * DEFAULT_FONTS[1])
        return (title_font, opt_font)

    def get_coords(self):
        TITLE_Y = 60
        
        # scale the parameters based on current resolution
        TESTED_RESOLUTION = 1920 * 1080
        w, h = pygame.display.get_surface().get_size()
        current_resolution = w * h
        if current_resolution != TESTED_RESOLUTION:
            scale = (current_resolution / TESTED_RESOLUTION)
            TITLE_Y = scale * TITLE_Y

        coords = []
        font_sizes = self.get_font_size()
        # determine title coordinates
        text_title = super().text_format(self.control_to_change, self.font, font_sizes[0], self.dark_red)
        title_w = text_title.get_rect().width
        title_h = text_title.get_rect().height
        title_x = (w - title_w) / 2
        coords.append((title_x, TITLE_Y))

        # determine text coordinates
        text_prompt = super().text_format(self.PROMPT_TEXT, self.font, font_sizes[1], self.black)
        prompt_w = text_prompt.get_rect().width
        prompt_h = text_prompt.get_rect().height
        prompt_x = (w - prompt_w) / 2
        prompt_y = (h - prompt_h) / 2
        coords.append((prompt_x, prompt_y))

        return coords

    def display(self):
        # Window display
        self.screen.fill(self.blue)
        title_font_size, text_size = self.get_font_size()
        
        # text formatting
        title = super().text_format(self.control_to_change, self.font, title_font_size, self.dark_red)

        prompt = super().text_format(self.PROMPT_TEXT, self.font, text_size, self.black)

        coords = self.get_coords()

        # insert title
        self.screen.blit(title, coords[0])

        # insert prompt
        self.screen.blit(prompt, coords[1])

        pygame.display.update()
        self.clock.tick(self.FPS)

    def destroy(self):
        self.screen.fill(self.blue)