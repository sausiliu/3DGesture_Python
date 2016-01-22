import pygame
import pygame.draw
import pygame.time

from math import sin, cos, acos


def project(self, v):
    pass


class Screen(object):
    def __init__(self, x=320, y=280, scale=1):
        self.i = pygame.display.set_mode((x, y))
        self.originx = self.i.get_width() / 2
        self.originy = self.i.get_height() / 2
        self.scale = scale


if __name__ == "__main__":
    pygame.init()
    screen = Screen()
