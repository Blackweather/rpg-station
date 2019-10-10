import pygame

class Window:
    """
    Parameters:
    title (string): text on the top of the window
    choices (List<string>): window options (exit will be added automatically)
    controls (dict<string, string>): default hotkey mappings
    """

    def init_pygame(self):
        # Colors
        self.white = (238, 238, 238)
        self.black = (17, 17, 17)
        self.gray = (50, 50, 50)
        self.red = (255, 0, 0)
        self.dark_red = (175, 78, 83)
        self.green = (0, 255, 0)
        self.blue = (69, 166, 185)  # light blue actually
        self.yellow = (255, 255, 0)
        # Fonts
        self.font = "./gui/font/OpenSans-Regular.ttf"

        # Game Framerate
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def text_format(self, message, text_font, text_size, text_color):
        new_font = pygame.font.Font(text_font, text_size)
        new_text = new_font.render(message, 0, text_color)
        return new_text
    """
    Description: class constructor for standarized rpg-station window

    Parameters:
    screen: pygame screen
    title(string): title of the window
    choices(list<string>): options available to choose in a window
    controls(list<?>): controls used to move through the window - not yet implemented
    extend_window(bool): flag to extend the window - half of the options will be used 
    as values and moved to the right side
    """
    def __init__(self, screen, title, choices, controls, extend_window=False):
        self.screen = screen
        self.title = title
        if not extend_window:
            self.choices = [*choices, "Exit"]
        else:
            # split the choices to choices and values
            tmp = choices[:len(choices)//2]
            self.values = choices[len(choices)//2:]
            self.choices = [*tmp, "Exit"]
            
        self.controls = controls
        # parameter for extended window - used for controls and hotkeys windows
        self.extend_window = extend_window
        if len(self.choices) > 0 and len(self.controls) > 0:
            self.init_pygame()
            #print("Initialized pygame in Window with title: " + self.title)
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
        DEFAULT_FONTS = (100, 70)
        w, h = pygame.display.get_surface().get_size()
        current_resolution = w * h
        if current_resolution == TESTED_RESOLUTION:
            return DEFAULT_FONTS

        # else calculate the fonts
        title_font = int((current_resolution / TESTED_RESOLUTION) * DEFAULT_FONTS[0])
        opt_font = int((current_resolution / TESTED_RESOLUTION) * DEFAULT_FONTS[1])
        return (title_font, opt_font)

    def get_coord_list(self, font_sizes):
        # scaling parameters
        TESTED_RESOLUTION = 1920 * 1080
        # minimum gap between the title and options/top of screen
        GAP = 60
        TITLE_Y = GAP

        # scale the parameters based on current resolution
        w, h = pygame.display.get_surface().get_size()
        current_resolution = w * h
        if current_resolution == TESTED_RESOLUTION:
            title_y = TITLE_Y
            gap_title = GAP
        else:
            scale = (current_resolution / TESTED_RESOLUTION)
            title_y = scale * TITLE_Y
            gap_title = scale * GAP

        coords = []
        # determine title coordinates
        text_title = self.text_format(self.title, self.font, font_sizes[0], self.dark_red)
        title_w = text_title.get_rect().width
        title_h = text_title.get_rect().height
        title_x = (w - title_w) / 2
        coords.append((title_x, title_y))

        # determine the position of the first option
        opt1_y = title_y + title_h + gap_title
        options_height = 0
        single_opt_height = 0
        gap = 0
        # scale the font and gaps between the options to fit
        while True:
            sample = self.text_format("Xp", self.font, font_sizes[1], self.black)
            # height of single option
            single_opt_height = sample.get_rect().height
            # number of options
            opt_num = len(self.choices)
            # space between y coordinate of two options
            gap = font_sizes[1] + 5
            # height of the option block
            options_height = single_opt_height + ((opt_num - 1) * gap)
            # available space for the option block
            space_for_opt = h - (2 * GAP) - title_h

            if options_height <= space_for_opt and options_height != 0:
                break
            # lower the font size if does not fit
            font_sizes[1] = font_sizes[1] - 1
        
        choice_num = 0
        # iterate through options
        for opt in self.choices:
            # check width for x coord
            choice_num += 1
            text_opt = self.text_format(opt, self.font, font_sizes[1], self.black)
            # determine the x coordinate of option
            text_w = text_opt.get_rect().width
            # check if extended here
            text_x = 0
            if not self.extend_window:
                text_x = (w - text_w) / 2
            else:
                text_x = ((w / 2) - text_w) / 2

            # determine the y coordinate of option
            opt1_centered_y = opt1_y + ((h - opt1_y - options_height - gap_title) / 2)
            text_y = opt1_centered_y + (choice_num - 1) * gap
            coords.append((text_x, text_y))

        choice_num = 0
        # iterate through values if extended
        if self.extend_window:
            # print("Choices: ", len(self.choices))
            # print("Values: ", len(self.values))
            for value in self.values:
                opt = str(value.replace('""', ''))
                #print(opt)
                # check width for x coord
                choice_num += 1
                text_opt = self.text_format(opt, self.font, font_sizes[1], self.black)
                # determine the x coordinate of option
                text_w = text_opt.get_rect().width
                # check if extended here
                text_x = (((w / 2) - text_w) / 2) + w / 2

                # determine the y coordinate of option
                opt1_centered_y = opt1_y + ((h - opt1_y - options_height - gap_title) / 2)
                text_y = opt1_centered_y + (choice_num - 1) * gap
                coords.append((text_x, text_y))

        return coords, font_sizes[1]

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
                        if selected == "Exit":
                            #print("Going back from the Window " + self.title)
                            self.destroy()
                            return "Exit"
                        else:
                            #print("Selection: " + selected)
                            self.destroy()
                            return selected
                    elif event.key == pygame.K_ESCAPE:
                        return "Exit"

            # Window display
            self.screen.fill(self.blue)
            title_font_size = self.get_font_size()[0]
            
            # text formatting
            title = self.text_format(self.title, self.font, title_font_size, self.dark_red)

            coords, opt_font_size = self.get_coord_list(font_sizes=list(self.get_font_size()))
            # options
            options_formatted = []
            for opt in self.choices:
                if selected == opt:
                    text_formatted = self.text_format(opt, self.font, opt_font_size, self.white)
                else:
                    text_formatted = self.text_format(opt, self.font, opt_font_size, self.black)
                options_formatted.append(text_formatted)

            if self.extend_window:
                for val in self.values:
                    text_formatted = self.text_format(val, self.font, opt_font_size, self.dark_red)
                    options_formatted.append(text_formatted)

            # get the list of coordinates
            options_with_coords = list(zip(options_formatted, coords[1:]))

            # insert title
            self.screen.blit(title, coords[0])

            # insert options
            for opt in options_with_coords:
                self.screen.blit(opt[0], opt[1])

            pygame.display.update()
            self.clock.tick(self.FPS)

    def destroy(self):
        # Quit pygame without quitting application
        self.screen.fill(self.blue)
        #print("Exited Window with title: " + self.title)
