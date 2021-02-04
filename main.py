from turtle import Screen, Turtle
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor('#000')
s.title("Snake Game")
s.tracer(0)


starting_postions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_postions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)



game_on = True

while game_on:
    s.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        x = segments[seg_num - 1].xcor()
        y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x, y)
    segments[0].forward(20)
    segments[0].right(90)
        





s.exitonclick()