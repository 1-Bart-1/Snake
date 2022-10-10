def convert_input(direction):
    if direction == 'w':
        return 0, -1  # x_speed, y_speed
    if direction == 's':
        return 0, 1
    if direction == 'a':
        return -1, 0
    if direction == 'd':
        return 1, 0

def overlapping(apple, segments):
    apple_pos = (apple.x, apple.y)
    head_pos = (segments[-1].x, segments[-1].y)
    segment_pos_list = [(segment.x, segment.y) for segment in segments]
    if head_pos == apple_pos:
        print("grow")
        return "grow"
    for i, segment_pos in enumerate(segment_pos_list):
        if head_pos == segment_pos and i != len(segments)-1:
            print("die")
            return "die"
    print("move")
    return "move"

def get_pixels(lights):
	pixels = []
	for row in lights:
		for light in row:
			pixels.append(light)
	return pixels
