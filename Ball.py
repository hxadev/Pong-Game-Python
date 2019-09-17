import turtle
import winsound


##
#
# Class that define the object of BAll
# @author Alfonso Hernandez Xochipa
# ##
class Ball:
    def __init__(self, speed, score):

        # Configuration of Ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.shapesize(stretch_wid=1, stretch_len=1)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.forward(100)

        # Attributes speed of the ball
        self.ball.dx = speed
        self.ball.dy = speed

        self.score = score
        self.score_a = self.score.get_score_a()
        self.score_b = self.score.get_score_b()

    def moveBall(self):

        self.ball.setx(self.ball.xcor()+self.ball.dx)
        self.ball.sety(self.ball.ycor()+self.ball.dy)

        # Define constraints of borders
        # Border Superior Check
        if(self.ball.ycor() > 290):
            self.ball.sety(290)
            self.ball.dy *= -1

        # Border inf check
        if(self.ball.ycor() < -290):
            self.ball.sety(-290)
            self.ball.dy *= -1

        # Border Rigth Point!!
        if(self.ball.xcor() > 390):
            winsound.Beep(2500,1000)
            if(self.score_a < 5):
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_a += 1
                self.score.clear()
                self.score.set_score_a(self.score_a)
                self.score.printScore()
            elif(self.score_a <= 5):
                turtle.done()
                self.finishScreen("A")

        # Border Left Point!!
        if(self.ball.xcor() < -390):
            winsound.Beep(2500,1000)
            if(self.score_b < 5):
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_b += 1
                self.score.clear()
                self.score.set_score_b(self.score_b)
                self.score.printScore()
            elif(self.score_b <= 5):
                turtle.done()
                self.finishScreen("B")

    def ballColitionOfThePaddle(self, paddle_a, paddle_b):
        if(
            (self.ball.xcor() > 340 and self.ball.xcor() < 350)
            and
            (self.ball.ycor() < paddle_b.getYPaddle() +
             40 and self.ball.ycor() > paddle_b.getYPaddle()-50)
        ):
            self.ball.setx(340)
            self.ball.dx *= -1

        if((self.ball.xcor() < -340 and self.ball.xcor() > -350) and (self.ball.ycor() < paddle_a.getYPaddle()+40 and self.ball.ycor() > paddle_a.getYPaddle()-50)):
            self.ball.setx(-340)
            self.ball.dx *= -1

    def getX(self):
        print("--X >> {}".format(self.ball.xcor()))
        return self.ball.xcor()

    def getY(self):
        print("--Y >> {}".format(self.ball.ycor()))

        return self.ball.ycor()

    def getDX(self):
        print(self.ball.dx)
        return self.ball.dx

    def getDY(self):
        print(self.ball.dy)
        # return self.ball.dy

    def finishScreen(self, playerWin):
        
        self.winner = turtle.Turtle()
        self.winner.speed(0)
        self.winner.color("white")
        self.winner.penup()
        self.winner.hideturtle()
        self.winner.goto(0, 0)
        self.winner.write("PLAYER {} WIN!!".format(playerWin), align="center", font=("Arial", 18, "bold"))
