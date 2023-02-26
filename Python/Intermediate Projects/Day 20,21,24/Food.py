import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        while random_x % 20 != 0:
            random_x = random.randint(-280, 280)
        while random_y % 20 != 0:
            random_y = random.randint(-280, 280)
        self.setpos(random_x, random_y)
