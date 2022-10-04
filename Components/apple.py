from random import randint


class Apple:
    def __init__(self, max):
        self.x = randint(0, max-1)
        self.y = randint(0, max-1)
        self.graphics = '0'

