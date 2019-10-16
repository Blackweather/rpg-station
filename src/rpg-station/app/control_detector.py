import pygame
from enum import EnumMeta

class ControlType(EnumMeta):
    KEYBOARD = "ControlType.KEYBOARD"
    BUTTON = "ControlType.BUTTON"
    HAT = "ControlType.HAT"
    AXIS = "ControlType.AXIS"

class Control:
    def __init__(self, control_type, number, value):
        self.control_type = control_type
        self.number = number
        if type(value) is list:
            self.value = tuple(value)
        else:
            self.value = value

    def __eq__(self, other):
        if type(other) is type(self):
            if self.control_type == ControlType.AXIS and other.control_type == ControlType.AXIS:
                if self.value < 0 and other.value < 0 and abs(self.value - other.value) < 0.1:
                    return True
                elif self.value > 0 and other.value > 0 and abs(self.value - other.value) < 0.1:
                    return True
                return False
            return vars(self) == vars(other)
        return False

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class ControlDetector:
    @staticmethod
    def detect_control():
        pygame.init()
        if pygame.joystick.get_count():
            j = pygame.joystick.Joystick(0)
            j.init()

        AXIS_MINIMUM_TRESHOLD = 0.8

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
