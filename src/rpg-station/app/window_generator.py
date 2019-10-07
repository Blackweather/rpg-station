import os
import glob
from .config_manager import ConfigManager
from .control_manager import ControlManager
from . import config

# class for holding single window parameters
class WindowParameters:
    def __init__(self, title, options, current_id, previous_id, extend_window=False):
        self.title = title
        self.options = options
        self.current_id = current_id
        self.previous_id = previous_id
        self.extend_window = extend_window

    def refresh_options(self, platform):
        cm = ControlManager(platform.lower())
        controls = cm.get_configurable_inputs()
        self.options = controls

class WindowGenerator:
    """
        Returns: platforms(List<String>) -
        non-empty platform directories
    """
    def define_platforms(self):
        platforms = []
        ROOT_ROM_DIR = config.RPG_ROOT + "/rom"
        for r,d,f in os.walk(ROOT_ROM_DIR):
            for _file in f:
                platforms.append(r.split('/')[-1].upper())
        return sorted(list(set(platforms)))

    """
        Returns: games(List<string>) -
            a list of games for the specified platform
    """
    def get_games(self, platform):
        ROOT_ROM_DIR = config.RPG_ROOT + "/rom/"
        game_dir = ROOT_ROM_DIR + platform.lower()
        cm = ConfigManager()
        cm.load_config()
        ext = cm.get_platform_extensions(platform)
        files_path = []
        for e in ext:
            flst = glob.glob(game_dir + '/*' + e)
            files_path.extend(flst)
        files = []
        for f in files_path:
            files.append(f.split('/')[-1])
        return sorted(files)


    """
        Returns: windows(List<WindowParameters>) -
            a list of windows defined in the application
    """
    def define_windows(self):
        windows = []
        TRAILING_SPACE = " "
        platforms = self.define_platforms()
        print (platforms)
        windows.append(WindowParameters(title="Raspberry Pi Gaming Station",
                                        options=["Start", "Controls", "Hotkeys"],
                                        current_id=1,
                                        previous_id=None))
        # pick a platform window
        windows.append(WindowParameters(title="Platforms",
                                        options=platforms,
                                        current_id=2,
                                        previous_id=1))
        # select platform for controls window
        windows.append(WindowParameters(title="Pick a platform",
                                        options=platforms,
                                        current_id=4,
                                        previous_id=1))
        # window for picking a platform to setup controls
        windows.append(WindowParameters(title="Controls",
                                        options=list(map(lambda x: x + TRAILING_SPACE, platforms)),
                                        current_id=5,
                                        previous_id=1))
        # TODO: fill this window with options
        # window for setting up menu hotkeys
        windows.append(WindowParameters(title="Hotkeys",
                                        options=["Save"],
                                        current_id=6,
                                        previous_id=1))
        # TODO: fill this window with options
        # window for setting up a new platform
        windows.append(WindowParameters(title="New Platform",
                                        options=["Save"],
                                        current_id=7,
                                        previous_id=1))
        curr_id = 7
        # Generate platform specific windows for games
        for plat in platforms:
            games = self.get_games(plat)
            curr_id += 1
            windows.append(WindowParameters(title=plat,
                                            options=games,
                                            current_id=curr_id,
                                            previous_id=2))
            # Platform control configuration window
            # TODO: create a function to get configurable controls for a specific platform
            #controls = self.get_control_options(plat)
            cm = ControlManager(plat.lower())
            controls = cm.get_configurable_inputs()
            # TRAILING_SPACE - workaround for windows to not be confused with platforms for games
            # TODO: add refresh of control values
            windows.append(WindowParameters(title=plat + TRAILING_SPACE,
                                            options=controls,
                                            current_id=curr_id + len(platforms),
                                            previous_id=5,
                                            extend_window=True))
        return windows

    def get_windowparameters_by_title(self, windows, title):
        for window_parameters in windows:
            if window_parameters.title == title:
                return WindowParameters(window_parameters.title,
                                       window_parameters.options,
                                       window_parameters.current_id,
                                       window_parameters.previous_id,
                                       window_parameters.extend_window)
        return None

    def get_windowparameters_by_id(self, windows, current_id):
        for window_parameters in windows:
            if window_parameters.current_id == current_id:
                return WindowParameters(window_parameters.title,
                                        window_parameters.options,
                                        window_parameters.current_id,
                                        window_parameters.previous_id,
                                        window_parameters.extend_window)
        return None

    