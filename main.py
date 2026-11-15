from turtle import *

def square(isBlack):
    if isBlack: color("black", "black")
    else: color("black", "white")

    begin_fill()
    for i in range(4):
        forward(50)
        left(90)
    end_fill()

def move(x, y):
    penup()
    goto(x, y)
    pendown()

startx = -200
starty = 0
move(startx, starty)


for j in range(3):
    for i in range(8):
        move(startx + (i + 1) * 50, starty + (j+1) * 50)
        square((i+j)%2==0)

exitonclick()