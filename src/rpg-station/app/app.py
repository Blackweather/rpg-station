from gui.window import Window
from gui.control_prompt import ControlPrompt
from .window_generator import WindowGenerator
from .game_runner import GameRunner
from .control_detector import ControlDetector, Control, ControlType
from .control_manager import ControlManager
from .hotkey_manager import HotkeyManager, create_hotkey_manager

import ctypes
import pygame
import time
import os

class App:
    def run(self):
        print("Initialized the application @app class")
        window_generator = WindowGenerator()
        windows = window_generator.define_windows()
        # set main menu as starting window
        current_params = window_generator.get_windowparameters_by_title(windows, "Raspberry Pi Gaming Station")
        # initalize pygame submodules
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
        pygame.init()
        # disable mouse cursor
        pygame.mouse.set_visible(0)
        # create a pygame default window
        info = pygame.display.Info()
        screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)
        while True:
            current_window = Window(screen=screen, 
                                    title=current_params.title, 
                                    choices=current_params.options, 
                                    extend_window=current_params.extend_window)
            result = current_window.display()
            if result == "Exit":
                current_params = window_generator.get_windowparameters_by_id(windows, current_params.previous_id)
                if current_params == None:
                    #TODO: ask to shutdown the system
                    break
            elif '.' in result:
                cm = ControlManager(platform=current_params.title.lower())
                cm.restore_control_config()
                # run a game
                gm = GameRunner(platform=current_params.title, file_name=result)
                gm.run()
            else:
                if result == "Start":
                    result = "Platforms"
                new_params = window_generator.get_windowparameters_by_title(windows, result)
                if new_params != None:
                    # if the window is a control window
                    current_params = new_params
                # figure out how to distinguish control from hotkeys
                elif current_params.title == "Hotkeys":
                    current_params.refresh_hotkeys()
                    # run control prompt
                    cw = ControlPrompt(screen, control_to_change=result)
                    cw.display()
                    # detect pressed control
                    control = ControlDetector.detect_control()
                    # run HotkeyManager to configure the json with hotkeys
                    hm = create_hotkey_manager()
                    hm.change_hotkey(opt=result, new_control=control)
                    cw.destroy()
                    current_params.refresh_hotkeys()

                elif current_params.extend_window:
                    # show a new window to prompt for controls
                    current_params.refresh_options(platform=current_params.title.replace(' ', '').lower())
                    cw = ControlPrompt(screen=screen,
                                        control_to_change=result)
                    cw.display()
                    # detect pressed control
                    control = ControlDetector.detect_control()
                    # platform is current window title minus the trailing space
                    cm = ControlManager(platform=current_params.title.replace(' ', '').lower())
                    cm.update_control_value(result, control)
                    # run ControlManager to configure the cfg file
                    # destroy the screen
                    cw.destroy()
                    current_params.refresh_options(platform=current_params.title.replace(' ', '').lower())

        pygame.display.quit()
        pygame.quit()
