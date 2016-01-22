import pygame
import pygame.draw
import pygame.time
from math import sin, cos, acos
from euclid import *

def project(self, v):
    pass

class Screen(object):
    def __init__(self, x=320, y=280, scale=1):
        self.i = pygame.display.set_mode((x, y))
        self.originx = self.i.get_width() / 2
        self.originy = self.i.get_height() / 2
        self.scale = scale

    def projetc(self, v):
        assert isinstance(v, Vector3)
        x = v.x * self.scale + self.originx
        y = v.y * self.scale + self.originy
        return (x, y)

    def depth(self, v):
        assert isinstance(v, Vector3)
        return v.z


class PrespectiveScreen(Screen):
    # the xy projection and depth functions are really an orthonormal space
    # but here i just approximated it with decimals to keep it quick n dirty
    def projetc(self, v):
        assert isinstance(v, Vector3)
        x = ((v.x * 0.975) + (v.z * 0.287)) * self.scale + self.originx
        y = ((v.y * 0.957) + (v.z * 0.287)) * self.scale + self.originy
        return (x, y)

if __name__ == "__main__":
    pygame.init()
    screen = Screen()
