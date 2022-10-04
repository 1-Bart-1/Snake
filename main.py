from sense_hat import SenseHat
from time import sleep
from pygame import event

from Components.snake import Snake
from Components.field import Field
from Components.apple import Apple

from Logic.logic import get_pixels

field_size = 8

field = Field(8)
snake = Snake()
apple = Apple(8)
sense = SenseHat()

def init():
    field.make_lights()
    snake.add_segment()

    return field.update_lights(snake.segments[0].x, snake.segments[0].y, snake.graphic)


def render():
    print("--------------------------")
#    field.print_lights()
    sense.set_pixels(get_pixels(field.lights))



def update():
    snake.move(direction)
    return field.update_lights(snake.segments[0].x, snake.segments[0].y, snake.graphic)


running = init()
while running:
	for event in event.get():
		if event.type == KEYDOWN:
			print("keydown")
    render()
    print(len(snake.segments))
    running = update()
	sleep(0.5)


