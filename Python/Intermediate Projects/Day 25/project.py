import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=725, height=490)
screen.bgpic(image)
bob = turtle.Turtle()
bob.penup()
bob.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

game_on = True
while game_on:
    user_guess = screen.textinput("Guess a state", "Please enter the name of a state: ").title()
    if user_guess == "exit":
        game_on = False
    elif len(guessed_states) != 50:
        if user_guess in states:
            guessed_states.append(user_guess)
            states.remove(user_guess)
            x_cor = int(data[data.state == user_guess].x)
            y_cor = int(data[data.state == user_guess].y)
            bob.goto(x_cor, y_cor)
            bob.write(user_guess)
        else:
            continue

screen.exitonclick()
