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
    speed = random.randint(4,10)
    turtle.forward(speed)

def turn():
    angle = random.randint(1,9) * 45
    turtle.setheading(angle)


turtle.Screen().bgcolor('blue')
turtle.pencolor('white')

while True:
    turn()
    move()
    contain()

