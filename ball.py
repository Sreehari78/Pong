from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.bounce_x_cor = 10
        self.bounce_y_cor = 10
        self.speed(0.1)
        self.movement_speed = 0.1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.bounce_x_cor
        new_y = self.ycor() + self.bounce_y_cor
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.bounce_y_cor *= -1

    def bounce_x(self):
        self.bounce_x_cor *= -1
        self.movement_speed *= 0.9
