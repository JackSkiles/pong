

import turtle
from random import seed
from random import randint

wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(350, 0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(-350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# square = turtle.Turtle()
# square.speed(0)
# square.shape("square")
# square.color("white")
# square.penup()
# square.goto(0, 0)
# game = 0

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .1
ball.dy = .1
running = True

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    # if(y == 300):
    #     y-= 1
    # else:
    #     y += 10
    y += 20
    paddle_b.sety(y)
    print("moved")

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    # if(y == -300):
    #     y += 1
    # else:
    #     y -= 10
    y -= 20
    paddle_b.sety(y)

def player2Move():
# generate some integers
    for _ in range(1):
        value = randint(0, 1)
        if value == 0:
            paddle_b_up()
            print(value)
        elif value == 1:
            print(value)
            paddle_b_down()
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
# wn.ontimer(player2Move, 2500)
# wn.ontimer(player2Move, 25)
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')
#Main game loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor () > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor () < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor () > 390:
        ball.setx(0)
        ball.dx *= -1
    if ball.xcor () < -390:
        ball.setx(0)
        ball.dx *= -1
