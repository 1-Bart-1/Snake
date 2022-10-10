from sense_hat import SenseHat
from time import sleep

from Components.snake import Snake
from Components.field import Field
from Components.apple import Apple

from Logic.logic import get_pixels, overlapping

direction = 'd'
field_size = 8
moving = False

field = Field(field_size)
snake = Snake()
apple = Apple(field_size)
sense = SenseHat()


def init():
	sense.set_imu_config(False, True, False)
	sense.clear(0, 0, 0)
	
	field.make_lights()
	snake.add_segment()
	
	return field.update_segment_lights(snake.segments, snake.graphic, apple)


def render():
    sense.set_pixels(get_pixels(field.lights))


def update():
	overlap = overlapping(apple, snake.segments)

	if overlap == "die":
		return False
	if overlap == "grow":
		apple.update()
		grow = True
	else:
		grow = False
	snake.move(direction, grow)

	return field.update_segment_lights(snake.segments, snake.graphic, apple)


def shutdown():
	sense.show_message("Game over", text_colour=(100, 100, 100))


running = init()
while running:
	for event in sense.stick.get_events():
		if event.action == "pressed":
			moving = True
			if event.direction == "right":
				direction = 'd'
			if event.direction == "left":
				direction = 'a'
			if event.direction == "up":
				direction = 'w'
			if event.direction == "down":
				direction = 's'
	if moving:
		running = update()
		render()
		sleep(0.5)
shutdown()