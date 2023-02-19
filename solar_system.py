import turtle
import time

# Set up the main screen and Turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Solar System")
t = turtle.Turtle()
t.speed(6)
# t.hideturtle()

# Define the function to draw a planet


def draw_planet(planet_color, planet_size, planet_distance):
    t.pencolor(planet_color)
    t.pensize(1)
    t.penup()
    t.forward(planet_distance)
    t.pendown()
    t.dot(planet_size)
    t.penup()
    t.backward(planet_distance)
    t.pencolor("white")
    t.penup()
    t.backward(planet_distance)
    t.right(90)
    t.pendown()
    t.circle(planet_distance)
    t.penup()
    t.left(90)
    t.forward(planet_distance)


# Draw the Sun
t.backward(500)
t.dot(400, "yellow")

# Draw the planets
draw_planet("gray", 7, 240)     # Mercury
draw_planet("orange", 9, 280)  # Venus
draw_planet("blue", 14, 320)   # Earth
draw_planet("red", 9, 360)    # Mars
draw_planet("goldenrod", 110, 520)   # Jupiter
draw_planet("tan", 80, 700)    # Saturn
draw_planet("lightblue", 50, 900)  # Uranus
draw_planet("lightgreen", 50, 1120)  # Neptune
# draw_planet("white", 4, 1000)   # Pluto

while True:
    t.penup()
    t.forward(0.1)
    t.backward(0.1)
