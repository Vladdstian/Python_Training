import time
from turtle import Screen, Turtle
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Vlad Snake Game")
screen.listen()

# Snake Setup
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Screen Listen commands
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.tracer(0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.update_scoreboard()
    snake.move_snake()

    # collision with food
    if snake.head.distance(food) < 13:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
