import turtle
from time import sleep

# Game Screen
win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score Counters
scoreA = 0
scoreB = 0

# Player A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.color("White")
paddleA.penup()
paddleA.goto(-350,0)

# Player B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.color("White")
paddleB.penup()
paddleB.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.05
ball.dy = 0.05

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0\tPlayer B : 0", align = "center", font = ("Courier", 20, "normal"))

# Player control functions
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Linking the Keyboard and Controls
win.listen()
win.onkeypress(paddleA_up, "w")
win.onkeypress(paddleA_down, "s")
win.onkeypress(paddleB_up, "Up")
win.onkeypress(paddleB_down, "Down")

# Main Game Loop
pen.goto(0, 0)
pen.write("WELCOME", align = "center", font = ("Courier", 29, "bold"))
sleep(2)
pen.clear()
pen.goto(0, 260)
while True:
    win.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
     
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A : {}\tPlayer B : {}".format(scoreA, scoreB), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= 1
        scoreB += 1
        pen.clear()
        pen.write("Player A : {}\tPlayer B : {}".format(scoreA, scoreB), align="center", font=("Courier", 20, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1