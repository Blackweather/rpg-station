from . import config
import os.path
import shutil
from collections import OrderedDict

class ControlManager:
    # TODO: this class should use the template to get option names
    # and actual config for option values
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
        platform_config_path = config.RPG_ROOT + "/src/config/controls/" + self._platform + "/config.cfg"

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