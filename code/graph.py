import math
from matplotlib import pyplot as plt
from datetime import datetime


class Graph:
    def __init__(self, object):
        self.object = object
        self.x = []
        self.y = []
        self.t = 0

    def take_points(self):
        self.x.append(self.t)
        self.y.append(self.object.rect.centery)
