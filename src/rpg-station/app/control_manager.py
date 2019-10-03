from . import config

class ControlManager:
    def load_template(self):
        # loads the template .conf as dictionary list
        template_path = config.RPG_ROOT + "/src/config/controls/template/config.cfg"
        template_content = []
        with open(template_path) as config_template:
            template_content = config_template.readlines()
        # strip whitespace characters and remove spaces
        template_content = [x.strip().replace(' ', '') for x in template_content]
        
        # transform to dictionary
        template_dict = {}
        for line in template_content:
            if line[0] != '#':
                config_value = line.split('=')
                template_dict[config_value[0]] = config_value[1]

        return template_dict

    def filter_joypad_indexes(self, text):
        JOYPAD_INDEX_TEXT = "joypad_index"

        if JOYPAD_INDEX_TEXT in text:
            return False
        else:
            return True

    def get_configurable_inputs_with_values(self):
        loaded_options = self.load_template()
        template_options = list(loaded_options.keys())
        # filter out joypad index options
        usable_options = filter(self.filter_joypad_indexes, template_options)
        # add values to filtered options
        result = {}
        for option in usable_options:
            result[option] = loaded_options[option]
        return result

    def get_configurable_inputs(self):
        # TODO: keep the order from template
        return sorted(list(self.get_configurable_inputs_with_values().keys()))

    def get_input_value(self, input):
        return self.load_template()[input]