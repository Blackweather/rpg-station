import json
from . import config

class ConfigManager:
    def load_config(self):
        # loads the config JSON as dictionary list
        config_path = config.RPG_ROOT + "/src/config/platforms.json"
        with open(config_path) as config_json:
            configuration = json.load(config_json)
            self.platforms = list(configuration.values())[0]
    def get_platform_names(self):
        names = []
        for p in self.platforms:
            names.append(p["platformName"])
        return names
    def get_platform_shorts_with_ext(self):
        # returns a dictionary
        # platformshort : extensions
        result = {}
        for p in self.platforms:
            result[p["platformShort"]] = p["extensions"]
        return result
    def get_platform_extensions(self, platform):
        plats = self.get_platform_shorts_with_ext()
        return plats[platform]

    def get_platform_shorts_with_core(self):
        # returns a dictionary
        # platformshort : core
        result = {}
        for p in self.platforms:
            result[p["platformShort"]] = p["coreName"]
        return result

    def get_platform_core(self, platform):
        plats = self.get_platform_shorts_with_core()
        return plats[platform]
    #TODO: create methods for changing/adding platforms and overwriting the config

