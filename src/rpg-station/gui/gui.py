import pygame
import os
from .window import Window

class Gui:

    def text_format(self, message, text_font, text_size, text_color):
        new_font = pygame.font.Font(text_font, text_size)
        new_text = new_font.render(message, 0, text_color)
        return new_text

    def run(self):
        print("Initialized the application @gui class")
        #TODO
        # Create a main menu window
        # Display it
        # Decide what to do next (returned by Window.display?)
        START_SCREEN_OPT = ["Start", "Controls", "Hotkeys"]
        start_screen = Window(title="Raspberry Pi Gaming Station", choices=START_SCREEN_OPT, controls=[""])
        start_screen.display()

