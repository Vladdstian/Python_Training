from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()


def move_forwards():
    bob.forward(10)

def move_backwards():
    bob.backward(10)

def turn_left():
    new_heading = bob.heading() + 10
    bob.setheading(new_heading)

def turn_right():
    new_heading = bob.heading() - 10
    bob.setheading(new_heading)

def clear():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
