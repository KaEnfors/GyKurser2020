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

def swirl(size, arc, points):
    for i in range(30):
        turtle.circle(size-i*3, arc, points)

turtle.speed(0)
turtle.pensize(3)

for i in range(100):
    turtle.color(random.choice(COLORS))
    turtle.penup()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.goto(x, y)
    turtle.pendown()
    swirl(90, 70, 10)

turtle.done()
