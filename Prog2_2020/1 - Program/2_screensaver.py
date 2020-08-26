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

def move(x:int, y:int):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def swirl(size, arc, points):
    size /= 2
    for i in range(13):
        turtle.circle(size-i*3, arc, points)

def triangle(size, **kwargs):
#    turtle.pensize(1)
    for i in range(11):
        turtle.forward(size-i*3 - i*5)
        turtle.left(120)

def star(size, **kwargs):
    for i in range(4):
        for j in range(5):
            turtle.forward(size - i*10)
            turtle.left(144)
        turtle.left(5)
turtle.speed(0)
turtle.pensize(2)

SHAPES = [
    triangle,
    swirl,
    star
]

for i in range(100):
    turtle.color(random.choice(COLORS))
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.setheading(random.randint(0,360))
    move(x, y)
    shapesize = random.randint(80,130)
    new_shape = random.choice(SHAPES)
    new_shape(size=shapesize, arc=120, points=30)


turtle.done()
