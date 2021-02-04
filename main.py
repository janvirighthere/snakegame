from turtle import Screen, Turtle
from snake import Snake
import time


# Screen settings 
WIDTH = 600
HEIGHT = 600
S_COLOR = "#000"

s = Screen()
s.setup(WIDTH, HEIGHT)
s.bgcolor(S_COLOR)
s.title("Snake Game")
s.tracer(0)


snake = Snake()

# Keybinds
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")



game_on = True

while game_on:
    s.update()
    time.sleep(0.1)

    snake.move()
    
    
        





s.exitonclick()