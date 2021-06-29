#Test comment
import turtle
import os

"""
wn = window
"""

#Setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0) #0 is the fastest
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Move the player left and right
def move_left():
    x = player.xcor() # Here I am taking the current value of x
    x -= playerspeed  # subtracting the speed (ie 15)
    player.setx(x)    # And giving the player a new position of the new value of x

def move_right():
    x = player.xcor()
    x += playerspeed
    player.setx(x)


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")








delay = input("Press enter to finish.")