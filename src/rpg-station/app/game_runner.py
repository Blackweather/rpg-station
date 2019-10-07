from . import config
from . config_manager import ConfigManager

import subprocess
import os

# this class takes care of starting up a ROM
class GameRunner:
    def __init__(self, platform, file_name):
        self.platform = platform
        self.file_name = file_name
        self.RUN_SCRIPT_PATH = config.RPG_ROOT + "/src/scripts/"
        self.RUN_SCRIPT_NAME = "run-game.sh"

    def get_full_path(self):
        return config.RPG_ROOT + "/rom/" + self.platform.lower() + "/" + self.file_name

    def get_libretro_core(self):
        cm = ConfigManager()
        cm.load_config()
        return cm.get_platform_core(self.platform)

    def run_script(self, path, core):
        print("Running command:")
        config_path = config.RPG_ROOT + "/src/config/controls/" + self.platform.lower() + "/config.cfg"
        print("/bin/bash -c " + self.RUN_SCRIPT_PATH + self.RUN_SCRIPT_NAME + " " + core + " \"" + path + "\"" +
            " \"" + config_path + "\"")
        arguments = self.RUN_SCRIPT_PATH + self.RUN_SCRIPT_NAME + " " + core + " \"" + path + "\"" + " \"" + config_path + "\""
        subprocess.Popen(['/bin/bash', '-c', arguments])

    def run(self):
        path = self.get_full_path()
        print ("Path=" + path)
        core = self.get_libretro_core()
        print ("Core=" + core)
        self.run_script(path, core)

