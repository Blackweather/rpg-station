import pygame
from os import system
pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                buttons = j.get_numbuttons()
                for i in range(buttons):
                    if j.get_button(i):
                        system('clear')
                        print("Pressed button " + str(i))
                        break
except KeyboardInterrupt:
    print("\nexiting now")
    j.quit()
