import pygame
from enum import Enum

class ControlType(Enum):
    KEYBOARD = 1
    BUTTON = 2
    HAT = 3
    AXIS = 4


class Control:
    def __init__(self, control_type, number, value):
        self.control_type = control_type
        self.number = number
        self.value = value


class ControlDetector:
    @staticmethod
    def detect_control():
        pygame.init()
        j = pygame.joystick.Joystick(0)
        j.init()

        AXIS_MINIMUM_TRESHOLD = 0.3

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    #rint("Pressed button " + str(event.button))
                    result = Control(ControlType.BUTTON, 0, event.button)
                    return result

                elif event.type == pygame.JOYHATMOTION:
                    #print("Moved hat #" + str(event.hat) + " with value: " + str(event.value))
                    result = Control(ControlType.HAT, event.hat, event.value)
                    return result

                elif event.type == pygame.JOYAXISMOTION:
                    #print("Moved axis #" + str(event.axis) + " with value: " + str(event.value))
                    # introduce minimum value to process the event to prevent accidental trigger
                    
                    if event.value >= AXIS_MINIMUM_TRESHOLD or event.value <= -AXIS_MINIMUM_TRESHOLD:
                        result = Control(ControlType.AXIS, event.axis, event.value)
                        return result

                elif event.type == pygame.KEYDOWN:
                    #print("Pushed keyboard button: " + str(pygame.key.name(event.key)))
                    result = Control(ControlType.KEYBOARD, 0, pygame.key.name(event.key))
                    return result
