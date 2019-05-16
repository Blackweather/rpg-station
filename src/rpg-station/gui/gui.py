import pygame
import os

class Gui:

    def text_format(self, message, text_font, text_size, text_color):
        new_font = pygame.font.Font(text_font, text_size)
        new_text = new_font.render(message, 0, text_color)
        return new_text

    def run(self):
        print("Initialized the application @gui class")
        pygame.init()
        # Set window parameters
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        gray = (50, 50, 50)
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        yellow = (255, 255, 0)

        # Fonts
        font = "./gui/font/OpenSans-Regular.ttf"

        # Game Framerate
        clock = pygame.time.Clock()
        FPS = 30

        selected = "start"
        is_quitting= False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "quit"
                    elif event.key == pygame.K_RETURN:
                        if selected == "start":
                            print("start")
                        if selected == "quit":
                            pygame.quit()
                            is_quitting = True

            if is_quitting:
                break

            # Main Menu UI
            screen.fill(blue)
            title = self.text_format("Raspberry Pi Gaming Station", font, 50, yellow)
            if selected == "start":
                text_start = self.text_format("START", font, 35, white)
            else:
                text_start = self.text_format("START", font, 35, black)

            if selected == "quit":
                text_quit = self.text_format("QUIT", font, 35, white)
            else:
                text_quit = self.text_format("QUIT", font, 35, black)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            screen.blit(title, (0, 80))
            screen.blit(text_start, (0, 300))
            screen.blit(text_quit, (0, 360))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Pygame simple main menu selection")
