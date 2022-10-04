class Field:
    def __init__(self, size):
        self.size = size
        self.lights = [[]]
        self.background = False
        self.gap = '  '

    def make_lights(self):
        for i in range(0, self.size):
            self.lights.append([])
            for j in range(0, self.size):
                self.lights[i].append(self.background)

    def reset_lights(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                self.lights[i][j] = self.background

    def update_lights(self, x, y, value):
        try:
            self.reset_lights()
            self.lights[y][x] = value
            return True
        except IndexError:
            print("Game over")
            return False

    def print_lights(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                print(self.lights[i][j], end=self.gap)
            print()

