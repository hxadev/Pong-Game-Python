import turtle

##
# 
# Class that define Object of the Score
# @author Alfonso Hernandez Xochipa
# ##
class Score:
    def __init__(self):
        self.score = turtle.Turtle()
        self.score.speed(0)
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 260)

        self.score_a = 0
        self.score_b = 0

    def printScore(self):
        self.score.write("A : {}      B:{}".format(
            self.score_a, self.score_b), align="center", font=("Arial", 18, "bold"))

    def clear(self):
        self.score.clear()

    def set_score_a(self, _score_a):
        self.score_a = _score_a

    def set_score_b(self, _score_b):
        self.score_b = _score_b

    def get_score_a(self):
        return self.score_a

    def get_score_b(self):
        return self.score_b
    
    
        
