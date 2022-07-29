from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.penup()
        self.x_move = 10   #An attribute or variable
        self.y_move = 10   #An attribute or variable
        self.move_speed = 0.1   #An attribute or variable

    def move(self):
        new_x = self.xcor() + self.x_move #An attribute
        new_y = self.ycor() + self.y_move #An attribute
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1 #Updating the y_move attribute

    def bounce_x(self):
        self.x_move *= -1  #Updating the x_move attribute
        self.move_speed *= 0.9  #Updating the move_speed attribute

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
