#Nousheen Siddiqui
#Edited on 02/11/2021
#Program is to draw and fill a polygon using turtle.



import turtle
nousheen = turtle.Turtle()
sides_poly = int (input("Sides of the Polygon"))
length_poly = int (input("Length of each side"))
color_poly = input("Mention the color")
nousheen.begin_fill()
nousheen.color(color_poly)
nousheen.fillcolor(color_poly)

wn = turtle.Screen()
angle = 360 / sides_poly
for i in range(sides_poly):
    nousheen.forward(length_poly)
    nousheen.left(angle)
nousheen.end_fill()