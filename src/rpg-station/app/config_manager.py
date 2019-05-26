import json

class ConfigManager:
    def load_config(self):
        # loads the config JSON as dictionary list
        with open("../../config/platforms.json") as config_json:
            config = json.load(config_json)
            self.platforms = list(config.values())[0]
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

    #TODO: create methods for changing/adding platforms and overwriting the config

# Sample usage
plats = ConfigManager()
plats.load_config()
print(plats.get_platform_shorts_with_ext())
