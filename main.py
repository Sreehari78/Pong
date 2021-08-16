import time
from turtle import Screen
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball

game_time = time
screen = Screen()
screen.setup(width=1366, height=700)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

pong_ball = Ball()
score = ScoreBoard()

player1_paddle = Paddle((660, 0))
player2_paddle = Paddle((-668, 0))

screen.onkey(fun=player1_paddle.go_up, key="Up")
screen.onkey(fun=player1_paddle.go_down, key="Down")

screen.onkey(fun=player2_paddle.go_up, key="w")
screen.onkey(fun=player2_paddle.go_down, key="s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(pong_ball.movement_speed)
    pong_ball.move()

    # Detect collision with top and bottom walls
    if pong_ball.ycor() > 320 or pong_ball.ycor() < -320:
        pong_ball.bounce_y()

    # Detect collision with right and left paddles
    if pong_ball.xcor() > 640 and pong_ball.distance(player1_paddle) < 50 or\
            pong_ball.xcor() < -648 and pong_ball.distance(player2_paddle) < 50:
        pong_ball.bounce_x()

    # Detect paddle misses and update score of player1
    if pong_ball.xcor() > 700:
        pong_ball.ball_reset()
        score.player_one_point()

    # Detect paddle misses and update score of player2
    if pong_ball.xcor() < -700:
        pong_ball.ball_reset()
        score.player_two_point()

    # Update the score and display it on screen
    score.update_score()

    # End game when a player scores 10 points
    if score.player_one_score == 10 or score.player_two_score == 10:
        game_is_on = False

screen.exitonclick()
