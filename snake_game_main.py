import turtle
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

# Create a screen
screen = Screen()
screen.screensize(600, 600, 'black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food_obj = Food()
score = Scoreboard()

turtle.listen()
# Control the snake
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

score.score_board_line()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food collision
    if snake.squares_list[0].distance(food_obj) < 15:
        food_obj.new_dot()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 320 or snake.head.xcor() < -320 or snake.head.ycor() > 235 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # Detect collision with tail.
    for squares in snake.squares_list[1:]:
        if snake.head.distance(squares) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
