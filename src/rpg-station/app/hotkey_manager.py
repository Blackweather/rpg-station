from . import config
from .control_detector import Control, ControlDetector

import json
import os


class HotkeyManager:
    def __init__(self, modified_controls=None, default_controls=None):
        if modified_controls != None:
            self.modified_controls = modified_controls
        else: modified_controls = {}

        if default_controls != None:
            self.default_controls = default_controls
        else: default_controls = {}

    @classmethod
    def from_json(cls, data):
        #dictionaries of option = control
        modified_controls = {}
        for controls in data['modified_controls'].items():
            modified_controls[controls[0]] = Control.from_json(controls[1])
        default_controls = {}
        for controls in data['default_controls'].items():
            default_controls[controls[0]] = Control.from_json(controls[1])

        return cls(modified_controls, default_controls)
    

    def get_opt_dict(self):
        opt_dict = {}
        for k,v in self.modified_controls.items():
            opt_dict[k] = v.value
        return opt_dict

    # first get dictionary of options from json and convert it to list compliant with extended options
    def get_opt_list(self):
        opts = self.get_opt_dict()
        return list(opts.keys()) + list(opts.values())


    def override_json(self, new_content):
        CONFIG_JSON = config.RPG_ROOT + "/src/config/hotkeys.json"
        with open(CONFIG_JSON, 'w') as f:
            f.write(new_content)
        

    def change_hotkey(self, opt, new_control):
        # modify the key in loaded dict
        self.modified_controls[opt] = new_control
        # deserialize the dict to the config json
        data = json.dumps(self, default=lambda x: x.__dict__, sort_keys=True, indent=4)
        self.override_json(data)

def create_hotkey_manager():
    CONFIG_JSON = config.RPG_ROOT + "/src/config/hotkeys.json"
    with open(CONFIG_JSON) as hotkey_json:
        data = json.load(hotkey_json)
    hm = HotkeyManager.from_json(data)
    return hm