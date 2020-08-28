import turtle
import time



turtle.shape('turtle')
#time.sleep(1)
turtle.speed(0)

#K
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
turtle.setheading(270)
turtle.forward(100)
turtle.left(165)
turtle.forward(110)
turtle.backward(110)
turtle.right(140)
turtle.forward(110)
turtle.backward(110)
turtle.right(25)
turtle.forward(100)

#A
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.setheading(250)
turtle.forward(230)
turtle.back(100)
turtle.setheading(0)
turtle.forward(60)
turtle.setheading(100)
turtle.forward(110)
turtle.back(230)

#LL
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.setheading(-90)
turtle.forward(200)
turtle.left(90)
turtle.forward(150)
turtle.backward(75)
turtle.left(90)
turtle.forward(200)

#E
turtle.penup()
turtle.goto(150, 100)
turtle.pendown()
turtle.setheading(180)
turtle.forward(75)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(50)
turtle.back(50)
turtle.right(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(70)

turtle.done()