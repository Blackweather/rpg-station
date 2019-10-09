import pygame
from os import system
pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                system('clear')
                print("Pressed button " + str(event.button))
            elif event.type == pygame.JOYHATMOTION:
                system('clear')
                print("Moved hat #" + str(event.hat) + " with value: "
                      + str(event.value))
            elif event.type == pygame.JOYAXISMOTION:
                system('clear')
                print("Moved axis #" + str(event.axis) + " with value: "
                      + str(event.value))
except KeyboardInterrupt:
    print("\nexiting now")
    j.quit()
