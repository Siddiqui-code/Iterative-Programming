#Nousheen Siddiqui
#2/12/2021
#Creates a cat using turtles.

import turtle
wn = turtle.Screen()
cat = turtle.Turtle()
cat.shape("turtle")
cat.color("black")
cat.fillcolor("yellow")
cat.begin_fill()
cat.pensize(5)
for i in range(20):
    cat.forward(20)
    cat.left(18)
cat.end_fill()
cat.fillcolor("goldenrod")
cat.begin_fill()
cat.pensize(5)
for i in range(20):
    cat.forward(35)
    cat.right(18)
cat.end_fill()
cat.penup()
for i in range(10):
    cat.forward(35)
    cat.right(18)
cat.right(180)
cat.pendown()
cat.pensize(10)
cat.forward(150)

    
