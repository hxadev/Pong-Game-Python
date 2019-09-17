import turtle

##
# 
# Class that define the object Paddle
# @author Alfonso Hernandez Xochipa
# ##
class Paddle:
    speed = 0

    def __init__(self, playerName, speed):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle.penup()

        self.speed = speed

        if(playerName == "A"):
            self.paddle.goto(-350, 0)
        elif(playerName == "B"):
            self.paddle.goto(350, 0)

    # Functions of paddles
    def paddle_up(self):
        y = self.paddle.ycor()
        y += self.speed
        if(y <= 240):
            self.paddle.sety(y)

        print("COR UP {}".format(y))

    def paddle_down(self):
        y = self.paddle.ycor()
        y -= self.speed
        if(y >= -220):
            self.paddle.sety(y)
        print("COR DOWN {}".format(y))

    def paddle_machine(self, ball_x, ball_y, ball_dx, level_machine):

        y = self.paddle.ycor()

        if(ball_y > self.paddle.ycor() and (ball_y >= 200 and ball_y+1 < 250)):
            if(y <= 240):
                self.paddle.sety(y+level_machine)
        if(ball_y < self.paddle.ycor() and (ball_y < 220 and ball_y-1 >= -220)):

            if(y >= -220):
                self.paddle.sety(y-level_machine)

        # if(ball_x > 320 and ball_dx > 0):
        #    if(ball_y > self.paddle.ycor() and self.paddle.ycor()+1 < 22):
        #        self.paddle.ycor += 1
        #    if(ball_y < self.paddle.ycor() and self.paddle.ycor()-1 > 4):
        #        self.paddle.ycor -= 1

    def setYPaddle(self, _y):
        self.paddle.sety(_y)

    def getYPaddle(self):
        return self.paddle.ycor()
