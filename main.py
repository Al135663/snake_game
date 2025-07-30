from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) ## Tracer turns the animation OFF or ON

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up") # when calling method. in the class don't use the parenthesis. snake.up
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # Detecting collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        is_game_on = False
        scoreboard.game_over()


    #Detect collision with tail.
    for segment in snake.segments[1:]: # by slicing snake head will not be included.
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()








screen.exitonclick()