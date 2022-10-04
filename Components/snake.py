from Logic.logic import convert_input
import logging

class Snake:
    def __init__(self):
        self.head_x = 0
        self.head_y = 0
        self.speed_x = 1
        self.speed_y = 0
        self.segments = []
        self.graphic = True

    def add_segment(self):
        self.segments.append(Segment())

    def move(self, direction):
        try:
            (self.speed_x, self.speed_y) = convert_input(direction)
        except TypeError:
            pass

        self.head_x += self.speed_x
        self.head_y += self.speed_y
        print(self.head_x, self.head_y)
        self.segments[0].x = self.head_x
        self.segments[0].y = self.head_y


class Segment(Snake):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.rank = 0

