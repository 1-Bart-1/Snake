from random import randint


class Apple:
    def __init__(self, max):
        self.max = max
        self.x = randint(0, self.max-1)
        self.y = randint(0, self.max-1)
        self.graphic = (150, 0, 0)


    def update(self):
        self.x = randint(0, self.max-1)
        self.y = randint(0, self.max-1)