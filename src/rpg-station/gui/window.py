import pygame

class Window:
    """
    Parameters:
    title (string): text on the top of the window
    choices (List<string>): window options (exit will be added automatically)
    controls (dict<string, string>): default hotkey mappings
    """
    def init_pygame(self):
        pygame.init()
        # Set window parameters
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (50, 50, 50)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        # Fonts
        self.font = "./gui/font/OpenSans-Regular.ttf"

        #Game Framerate
        self.clock = pygame.time.Clock()
        self.FPS = 30

    def text_format(self, message, text_font, text_size, text_color):
        new_font = pygame.font.Font(text_font, text_size)
        new_text = new_font.render(message, 0, text_color)
        return new_text

    def __init__(self, title, choices, controls):
        self.title = title
        self.choices = choices
        self.controls = controls
        if len(self.choices) > 0 and len(self.controls) > 0:
            self.init_pygame()
            print("Initialized pygame in Window with title: " + self.title)
        else:
            print("Bad arguments in Window constructor")

    def display(self):
        # Window loop
        pass

    def destroy(self):
        # Quit pygame without quitting application
        pass


