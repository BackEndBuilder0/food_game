from turtle import Turtle

POSITION_TURTLES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.squares_list = []
        self.create_snake()
        self.head = self.squares_list[0]

    # Create a snake body
    def create_snake(self):
        for position in POSITION_TURTLES:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        new_square.speed('fastest')
        self.squares_list.append(new_square)

    # Extend the snake size after eating food
    def extend(self):
        self.add_segment(self.squares_list[-1].position())

    # Moving the turtle
    def move(self):
        for squares_num in range(len(self.squares_list) - 1, 0, -1):
            x_cor = self.squares_list[squares_num - 1].xcor()
            y_cor = self.squares_list[squares_num - 1].ycor()
            self.squares_list[squares_num].goto(x_cor, y_cor)
        self.squares_list[0].forward(MOVE_DISTANCE)

    # Control rules for snake
    def up(self):
        if int(self.squares_list[0].heading()) != 270:
            self.squares_list[0].setheading(90)

    def down(self):
        if int(self.squares_list[0].heading()) != 90:
            self.squares_list[0].setheading(270)

    def left(self):
        if int(self.squares_list[0].heading()) != 0:
            self.squares_list[0].setheading(180)

    def right(self):
        if int(self.squares_list[0].heading()) != 180:
            self.squares_list[0].setheading(0)
