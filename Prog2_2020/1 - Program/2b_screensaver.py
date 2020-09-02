import turtle, random

COLORS = [
    'red',
    'blue',
    'purple',
    'indigo',
    'green',
    'yellow',
    'pink',
]

TOP = 200
BOTTOM = -200
LEFT = -200
RIGHT = 200

def contain():
    global TOP, BOTTOM, LEFT, RIGHT
    
    if turtle.xcor() < LEFT:
        turtle.goto(turtle.xcor() + 40, turtle.ycor())
    elif turtle.xcor() > RIGHT:
        turtle.goto(turtle.xcor() - 40, turtle.ycor())
    
    if turtle.ycor() < BOTTOM:
        turtle.goto(turtle.xcor(), turtle.ycor() + 40)
    elif turtle.ycor() > TOP:
        turtle.goto(turtle.xcor(), turtle.ycor() - 40)

def move():
    speed = random.randint(20,40)
    turtle.forward(speed)

def turn():
    angle = random.randint(0,4) * 90
    turtle.setheading(angle)


turtle.Screen().bgcolor('blue')
turtle.pencolor('white')
turtle.speed(0)
turtle.pensize(5)

counter = 0

while True:
    turn()
    move()
    contain()
    counter += 1
    if counter > 100:
        turtle.pencolor(random.choice(COLORS))
        turtle.Screen().bgcolor(random.choice(COLORS))
        counter = 0

