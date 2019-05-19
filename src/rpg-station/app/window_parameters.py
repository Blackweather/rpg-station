# class for holding single window parameters
class WindowParameters:
    def __init__(self, title, options, current_id, previous_id):
        self.title = title
        self.options = options
        self.current_id = current_id
        self.previous_id = previous_id
