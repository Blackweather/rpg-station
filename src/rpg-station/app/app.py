from gui.window import Window
from .window_generator import WindowGenerator
from .game_runner import GameRunner
import ctypes

import pygame

class App:
    def run(self):
        print("Initialized the application @app class")
        window_generator = WindowGenerator()
        windows = window_generator.define_windows()
        # set main menu as starting window
        current_params = window_generator.get_windowparameters_by_title(windows, "Raspberry Pi Gaming Station")
        # initalize pygame submodules
        pygame.init()
        # disable mouse cursor
        pygame.mouse.set_visible(0)
        # create a pygame default window
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        while True:
            current_window = Window(screen=screen, title=current_params.title, choices=current_params.options, controls=[""])
            result = current_window.display()
            if result == "Exit":
                current_params = window_generator.get_windowparameters_by_id(windows, current_params.previous_id)
                if current_params == None:
                    break
            elif '.' in result:
                #run a game
                gm = GameRunner(platform=current_params.title, file_name=result)
                gm.run()
            else:
                if result == "Start":
                    result = "Platforms"
                new_params = window_generator.get_windowparameters_by_title(windows, result)
                if new_params != None:
                    current_params = new_params
        pygame.display.quit()
        pygame.quit()
