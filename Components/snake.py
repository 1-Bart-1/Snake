from Logic.logic import convert_input


class Snake:
	def __init__(self):
		self.head_x = 4
		self.head_y = 4
		self.speed_x = 1
		self.speed_y = 0
		self.segments = []
		self.graphic = (100, 100, 100)

	def add_segment(self):
		self.segments.append(Segment(0, 0))

	def move(self, direction, grow):
		(self.speed_x, self.speed_y) = convert_input(direction)
		
		self.head_x += self.speed_x
		self.head_y += self.speed_y
		
		self.segments.append(Segment(self.head_x, self.head_y))
		
		if not grow:
			self.segments.pop(0)


class Segment(Snake):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
