import turtle
import time

my_turtle = turtle.Turtle()

pedals = int(input("Enter the number of petals (must be an even number): "))
stem_angle = 180 - (360 / pedals)

stem_length = int(input("Enter the length of stem: "))
type = input("Enter the petal type (triangle, square, or pentagon): ")

angle = 0
sides = 0
if type == "triangle":
    sides = 3
elif type == "square":
    sides = 4
else:
    sides = 5

angle = 360 / sides
start_angle = (180 - angle) / 2

side_length = int(input("Enter the length of side: "))
stem_color = input("Enter the stem colour: ")
first_pedal_color = input("Enter the first petal colour: ")
second_pedal_color = input("Enter the second petal colour: ")

my_turtle.left(90)

for i in range(0, pedals):
    my_turtle.color(stem_color)
    my_turtle.forward(stem_length)
    my_turtle.left(start_angle)
    if i % 2 == 0:
        my_turtle.color(first_pedal_color)
    else:
        my_turtle.color(second_pedal_color)
    my_turtle.forward(side_length)
    for a in range(1, sides):
        my_turtle.right(angle)
        my_turtle.forward(side_length)
    my_turtle.left(start_angle)
    my_turtle.color(stem_color)
    my_turtle.forward(stem_length)
    my_turtle.left(stem_angle)

time.sleep(10)
'''6
50
triangle
100
green
blue
yellow'''