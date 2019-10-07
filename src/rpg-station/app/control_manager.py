from . import config
from .control_detector import Control, ControlType

import os
import os.path
import shutil
import fileinput
import re
from collections import OrderedDict

class ControlManager:
    def __init__(self, platform):
        self._platform = platform

    def load_template(self):
        # loads the template .conf as dictionary list
        template_path = config.RPG_ROOT + "/src/config/controls/template/config.cfg"
        template_content = []
        with open(template_path) as config_template:
            template_content = config_template.readlines()
        # strip whitespace characters and remove spaces
        template_content = [x.strip().replace(' ', '') for x in template_content]

        # determine actual config
        platform_config_path = config.RPG_ROOT + "/src/config/controls/" + self._platform + "/backup/"

        if not os.path.exists(platform_config_path):
            os.makedirs(platform_config_path)

        platform_config_path += "config.cfg"

        if not os.path.exists(platform_config_path):
            shutil.copyfile(template_path, platform_config_path)

        platform_config_content = []
        with open(platform_config_path) as platform_config:
            platform_config_content = platform_config.readlines()

        platform_config_content = [x.strip().replace(' ', '') for x in platform_config_content]

        platform_dict = OrderedDict()
        for line in platform_config_content:
            if '=' in line:
                config_value = line.split('=')
                platform_dict[config_value[0]] = config_value[1]
        
        # transform to dictionary
        result_dict = OrderedDict()
        for line in template_content:
            if line[0] != '#' and "joypad_index" not in line:
                config_value = line.split('=')
                result_dict[config_value[0]] = platform_dict[config_value[0]]

        return result_dict

    def get_configurable_inputs_with_values(self):
        loaded_options = self.load_template()
        template_options = list(loaded_options.keys())
        # add values to filtered options
        result = OrderedDict()
        for option in template_options:
            result[option] = loaded_options[option]
        return result

    def get_configurable_inputs(self):
        inputs_with_values = self.get_configurable_inputs_with_values()
        return list(inputs_with_values.keys()) + list(inputs_with_values.values())

    def get_input_value(self, input):
        return self.load_template()[input]

    def convert_hat(self, control):
        direction = ""
        if control.value == (0, -1):
            direction = "down"
        elif control.value == (0, 1):
            direction = "up"
        elif control.value == (-1, 0):
            direction = "left"
        elif control.value == (1, 0):
            direction = "right"
        
        result = "h" + str(control.number) + direction

        return result

    def convert_axis(self, control):
        sign = ""
        if control.value < 0:
            sign = "-"
        else:
            sign = "+"

        result = sign + str(control.number)
        return result

    # converts pygame generated controls to RetroArch convention compliant controls
    def convert_control_value(self, control):
        if control.control_type == ControlType.KEYBOARD:
            return str(control.value)
        elif control.control_type == ControlType.BUTTON:
            return str(control.value)
        elif control.control_type == ControlType.HAT:
            return self.convert_hat(control)
        elif control.control_type == ControlType.AXIS:
            return self.convert_axis(control)
        else:
            return None

    def is_compliant(self, control, field):
        if "btn" in field and control.control_type not in [ControlType.BUTTON, ControlType.HAT]:
            print("Cannot assign anything else than a button/hat to that field")
            return False
        if "axis" in field and control.control_type != ControlType.AXIS:
            print("Cannot assign anything else than an axis to that field")
        return True

    def update_value_in_file(self, field, value):
        platform_config_path = config.RPG_ROOT + "/src/config/controls/" + self._platform + "/backup/config.cfg"

        search = str(field) + " = .*"
        replace = str(field) + " = \"" + str(value) + "\""

        for line in fileinput.input(platform_config_path, inplace=True):
            result = re.sub(search, replace, line.rstrip())
            print(result)
        

    # updates the value of a single control in the .cfg file of a specific platform
    def update_control_value(self, field, control):
        if self.is_compliant(control, field):
            # convert the control to use the RetroArch specific values
            converted = self.convert_control_value(control)
            if converted == None:
                print('Something went wrong with your controls')
                return
            # override the value in .conf file of the platform
            self.update_value_in_file(field, converted)

    def restore_control_config(self):
        # delete the config.cfg in platform directory and copy the one in backup directory
        backup_path = config.RPG_ROOT + "/src/config/controls/" + self._platform + "/backup/config.cfg"
        platform_config_path = config.RPG_ROOT + "/src/config/controls/" + self._platform + "/config.cfg" 

        if os.path.isfile(platform_config_path):
            os.remove(platform_config_path)
        if os.path.isfile(backup_path):
            shutil.copyfile(backup_path, platform_config_path)
