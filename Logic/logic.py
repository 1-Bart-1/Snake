def convert_input(direction):
    if direction == 'w':
        return 0, -1  # x_speed, y_speed
    if direction == 's':
        return 0, 1
    if direction == 'a':
        return -1, 0
    if direction == 'd':
        return 1, 0

def check_overlapping(pos1, pos2):
    if pos1 == pos2:
        return True
    return False

def get_pixels(lights):
	pixels = []
	for row in lights:
		for light in row:
			if light == True:
				pixels.append((100, 100, 100))
			else:
				pixels.append((0, 0, 0))
	return pixels
