import turtle
from Paddle import Paddle
from Ball import Ball
from Score import Score
import os
import winsound
from threading import Thread

##
# Class Principal of the Game Pong
# @author Alfonso Hernandez Xochipa
# ##


class PongPlayer:

    # CONSTANTS
    __SPEED_PLADDE = 30
    __SPEED_BALL = 0.5
    __SCORE_A = __SCORE_B = 0

    # Attributes paddle
    paddle_a = 0
    paddle_b = 0
    level = "N"

    def __init__(self):
        # Construct the principal Screen
        self.wn = turtle.Screen()
        self.wn.title("PONG GAME HERNANDEZ X.A")
        # self.wn.bgcolor("black")
        self.wn.bgpic("bg_game.gif")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

        # Construct Threads
        self.threadMusic = Thread(target=self.playMusicBack)
        self.threadMusic.start()

        # construct Paddles
        self.paddle_a = Paddle("A", PongPlayer.__SPEED_PLADDE)
        self.paddle_b = Paddle("B", PongPlayer.__SPEED_PLADDE)

        # Construrct the Score fo the players
        self.score = Score()
        self.score.printScore()

        # Construct of Ball
        self.ball = Ball(PongPlayer.__SPEED_BALL, self.score)

    def mainTwoPlayers(self):

        self.wn.listen()

        self.wn.onkeypress(self.paddle_a.paddle_up, ("w"))
        self.wn.onkeypress(self.paddle_a.paddle_down, ("s"))

        self.wn.onkeypress(self.paddle_b.paddle_up, ("Up"))
        self.wn.onkeypress(self.paddle_b.paddle_down, ("Down"))

        while 1:
            # Update the screen while the loop is 1 o true
            self.wn.update()

            # Funtion to move ball
            self.ball.moveBall()
            self.ball.ballColitionOfThePaddle(self.paddle_a, self.paddle_b)

    def mainMachinePlayer(self, level):

        if(level == "F" or level == "f"):
            PongPlayer.__SPEED_BALL = 0.2
            levelMachine = 2
        if(level == "d" or level == "D"):
            PongPlayer.__SPEED_BALL = 2
            levelMachine = 3
        if(level == "E" or level == "e"):
            PongPlayer.__SPEED_BALL = 5
            levelMachine = 5

        print("Player with the machine")
        self.wn.listen()

        self.wn.onkeypress(self.paddle_a.paddle_up, ("w"))
        self.wn.onkeypress(self.paddle_a.paddle_down, ("s"))
        while 1:
            self.wn.update()
            self.ball.moveBall()
            self.ball.ballColitionOfThePaddle(self.paddle_a, self.paddle_b)
            _x = self.ball.getX()
            _y = self.ball.getY()
            _dx = self.ball.getDX()

            self.paddle_b.paddle_machine(_x, _y, _dx, levelMachine)

    def playMusicBack(self):
        winsound.PlaySound("POL-star-way-short.wav",
                           winsound.SND_LOOP+winsound.SND_ASYNC)
