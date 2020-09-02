import turtle, random


TOP = 200
BOTTOM = -200
LEFT = -200
RIGHT = 200

def contain():
    global TOP, BOTTOM, LEFT, RIGHT
    
    if turtle.xcor() < LEFT:
        turtle.goto(turtle.xcor() + 10, turtle.ycor())
    elif turtle.xcor() > RIGHT:
        turtle.goto(turtle.xcor() - 10, turtle.ycor())
    
    if turtle.ycor() < BOTTOM:
        turtle.goto(turtle.xcor(), turtle.ycor() + 10)
    elif turtle.ycor() > TOP:
        turtle.goto(turtle.xcor(), turtle.ycor() - 10)

def move():
    

while True:

