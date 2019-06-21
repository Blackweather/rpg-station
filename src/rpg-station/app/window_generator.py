import os

# class for holding single window parameters
class WindowParameters:
    def __init__(self, title, options, current_id, previous_id):
        self.title = title
        self.options = options
        self.current_id = current_id
        self.previous_id = previous_id
class WindowGenerator:
    """
        Returns: platforms(List<String>) -
        non-empty platform directories
    """
    def define_platforms(self):
        platforms = []
        ROOT_ROM_DIR = "../../rom"
        print(os.walk(ROOT_ROM_DIR))
        for r,d,f in os.walk(ROOT_ROM_DIR):
            for _file in f:
                platforms.append(r.split('/')[-1].upper())
        return sorted(list(set(platforms)))
    """
        Returns: windows(List<WindowParameters>) -
            a list of windows defined in the application
    """
    def define_windows(self):
        windows = []
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
        # TODO: change to actual game list
        # pick a game window
        windows.append(WindowParameters(title="Games",
                                        options=["Mario","Pokemon","GTA"],
                                        current_id=3,
                                        previous_id=2))
        # select platform for controls window

        windows.append(WindowParameters(title="Pick a platform",
                                        options=platforms,
                                        current_id=4,
                                        previous_id=1))
        # TODO: change the title to Controls-$PLATFORM
        # window for setting up controls for specific platform
        windows.append(WindowParameters(title="Controls",
                                        options=["Save"],
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
                                        previous_id=2))
        return windows


    def get_windowparameters_by_title(self, windows, title):
        for window_parameters in windows:
            if window_parameters.title == title:
                return WindowParameters(window_parameters.title,
                                       window_parameters.options,
                                       window_parameters.current_id,
                                       window_parameters.previous_id)
        return None

    def get_windowparameters_by_id(self, windows, current_id):
        for window_parameters in windows:
            if window_parameters.current_id == current_id:
                return WindowParameters(window_parameters.title,
                                        window_parameters.options,
                                        window_parameters.current_id,
                                        window_parameters.previous_id)
        return None
