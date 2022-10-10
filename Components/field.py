class Field:
	def __init__(self, size):
		self.size = size
		self.lights = [[]]
		self.background = (0, 0, 0)
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

	def update_segment_lights(self, segments, value, apple):
		self.reset_lights()
		self.update_apple_lights(apple)
		
		in_bounds = True
		for segment in segments:
			if 0 <= segment.x < self.size and 0 <= segment.y < self.size:
				self.lights[segment.y][segment.x] = value
			else:
				return False
		return True


	def update_apple_lights(self, apple):
		x = apple.x
		y = apple.y
		value = apple.graphic
		self.lights[y][x] = value

