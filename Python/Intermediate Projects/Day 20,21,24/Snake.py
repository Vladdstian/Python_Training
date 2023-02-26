from turtle import Turtle

SEGMENTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_body()
        self.head = self.body[0]

    def create_body(self):
        for pos in SEGMENTS:
            self.add_segment(pos)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.setpos(position)
        self.body.append(new_turtle)

    def extend(self):
        new_pos = (self.body[-1].xcor(), self.body[-1].ycor())
        self.add_segment(new_pos)

    def move_snake(self):
        for segment_num in range(len(self.body)-1, 0, -1):
            new_x = self.body[segment_num - 1].xcor()
            new_y = self.body[segment_num - 1].ycor()
            self.body[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.body:
            segment.goto(1000, 1000)
        self.body.clear()
        self.create_body()
        self.head = self.body[0]
