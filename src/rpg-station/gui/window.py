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
        self.blue = (173, 216, 230)  # light blue actually
        self.yellow = (255, 255, 0)
        # Fonts
        self.font = "./gui/font/OpenSans-Regular.ttf"

        # Game Framerate
        self.clock = pygame.time.Clock()
        self.FPS = 30

    def text_format(self, message, text_font, text_size, text_color):
        new_font = pygame.font.Font(text_font, text_size)
        new_text = new_font.render(message, 0, text_color)
        return new_text

    def __init__(self, title, choices, controls):
        self.title = title
        self.choices = [*choices, "exit"]
        self.controls = controls
        if len(self.choices) > 0 and len(self.controls) > 0:
            self.init_pygame()
            print("Initialized pygame in Window with title: " + self.title)
        else:
            print("Bad arguments in Window constructor")

    """
    Description:
    
    Parameters:
    number(int): current index of the list
    length(int): length of the list
    change(int): step to change the list element
    
    Return:
    index(int): index of the previous/next element
    """

    def switch_selection(self, number, length, change):
        if change < 0:
            if number == 0:
                return length - 1
            else:
                return number - 1
        elif number == length - 1:
            return 0
        else:
            return number + 1

    def get_font_size(self):
        """
        Description:
        Calculates font sizes based on current resolution
        Returns:
        font_sizes(tuple<int, int>): font sizes of title and options
        """
        TESTED_RESOLUTION = 1920 * 1080
        TESTED_FONTS = (100, 70)
        w, h = pygame.display.get_surface().get_size()
        current_resolution = w * h
        if current_resolution == TESTED_RESOLUTION:
            return TESTED_FONTS

        # else calculate the fonts
        title_font = (current_resolution / TESTED_RESOLUTION) * TESTED_FONTS[0]
        opt_font = (current_resolution / TESTED_RESOLUTION) * TESTED_FONTS[1]

        return (title_font, opt_font)

    def get_coord_list(self, font_sizes):
        # scaling parameters
        TESTED_RESOLUTION = 1920 * 1080
        TITLE_Y = 80
        # y of first option (not centered)
        OPT1_Y = 300
        # gap between two options
        GAP = 80
        w, h = pygame.display.get_surface().get_size()
        current_resolution = w * h
        if current_resolution == TESTED_RESOLUTION:
            title_y = TITLE_Y
            opt1_y = 300
            gap = GAP
        else:
            scale = (current_resolution / TESTED_RESOLUTION)
            title_y = scale * TITLE_Y
            opt1_y = scale * OPT1_Y
            gap = scale * GAP

        coords = []

        # pick the title
        # check width for x coords
        text_title = self.text_format(self.title, self.font, font_sizes[0], self.yellow)
        title_w = text_title.get_rect().width
        title_x = (w - title_w) / 2
        coords.append((title_x, title_y))

        # get height of all options
        sample = self.text_format("X", self.font, font_sizes[1], self.black)
        opt_text_height = sample.get_rect().height
        options_height = len(self.choices) * opt_text_height + \
                         (len(self.choices) - 1) * gap
        choice_num = 0
        # iterate through options
        for opt in self.choices:
            # check width for x coord
            choice_num += 1
            text_opt = self.text_format(opt, self.font, font_sizes[1], self.black)
            text_w = text_opt.get_rect().width
            text_x = (w - text_w) / 2

            # calculate the y coord for current option
            opt1_centered_y = opt1_y + (h - opt1_y - options_height) / 2
            text_y = opt1_centered_y + (choice_num - 1) * gap
            coords.append((text_x, text_y))

        return coords

    def display(self):
        """
        Returns:
        new_title (string): name of the next window 
        or "exit" in case of going back
        """
        # Window loop
        selected = self.choices[0]
        selected_index = 0
        while True:
            # handling key events
            for event in pygame.event.get():
                # TODO: support multiple control options
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_index = self.switch_selection(selected_index, len(self.choices), -1)
                        selected = self.choices[selected_index]
                    elif event.key == pygame.K_DOWN:
                        selected_index = self.switch_selection(selected_index, len(self.choices), 1)
                        selected = self.choices[selected_index]
                    elif event.key == pygame.K_RETURN:
                        if selected == "exit":
                            print("Going back from the Window " + self.title)
                            self.destroy()
                            return "exit"
                        else:
                            print("Selection: " + selected)
                            self.destroy()
                            return selected

            # Window display
            self.screen.fill(self.blue)
            # TODO: count positions for text
            title_font_size, opt_font_size = self.get_font_size()
            # text formatting
            title = self.text_format(self.title, self.font, title_font_size, self.yellow)

            # options
            options_formatted = []
            for opt in self.choices:
                if selected == opt:
                    text_formatted = self.text_format(opt, self.font, opt_font_size, self.white)
                else:
                    text_formatted = self.text_format(opt, self.font, opt_font_size, self.black)
                options_formatted.append(text_formatted)

            # get the list of coordinates
            coords = self.get_coord_list(font_sizes=(title_font_size, opt_font_size))
            options_with_coords = list(zip(options_formatted, coords))

            for opt in options_with_coords:
                self.screen.blit(opt[0], opt[1])

            pygame.display.update()
            self.clock.tick(self.FPS)

    def destroy(self):
        # Quit pygame without quitting application
        pygame.display.quit()
        pygame.quit()
        print("Exited Window with title: " + self.title)
