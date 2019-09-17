import turtle
from Pong import PongPlayer


##
# 
# Main of the Game
# @author Alfonso Hernandez Xochipa
# ##

### Attributes
image = "pongPortada.gif"
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgpic(image)

screen.title("Pong Game @HernandezXA")

# Events Fuctinos
def playGameTwoPlayers():
    screen.clear()
    pong = PongPlayer()
    pong.mainTwoPlayers()

def playGameWithMachine():
    screen.clear()
    level=ScreenDificult()
    print(level)
    pong = PongPlayer()
    pong.mainMachinePlayer(level)


def ScreenDificult():
    screen.clear()
    screenD=turtle.Screen()
    screenD.bgcolor("black")
    screenD.tracer(0)
    dificult = turtle.Turtle()
    dificult.speed(0)
    dificult.color("white")
    dificult.penup()
    dificult.hideturtle()
    dificult.goto(0, 0)
    dificult.write(
    """SELECCIONA EL NIVEL
        F)FACIL
        D)DIFICL
        E)EXTREMO""",align="center", font=("Arial", 18, "bold"))
    
    screenD.listen()
    level=screenD.textinput("Nivel","""SELECCIONA EL NIVEL
        F)FACIL
        D)DIFICL
        E)EXTREMO""")
    screenD.clear()
    dificult.clear()

    return level
    
    
####################### Events
screen.listen()
screen.onkeypress(playGameTwoPlayers, ("1"))
screen.onkeypress(playGameWithMachine, ("2"))


screen.mainloop()
