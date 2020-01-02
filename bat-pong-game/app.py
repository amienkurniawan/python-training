import turtle
import winsound

Player_A = input('enter name first player : ')
Player_B = input('enter name Second player : ')

wn = turtle.Screen()
wn.title("pong by amien kurniawan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# score
score_A = 0
score_B = 0
# a = 0
# b = 0
# paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.penup()
paddle_A.goto(-350,0)
paddle_A.shapesize(stretch_len=1,stretch_wid=5)

# paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(350,0)
paddle_B.shapesize(stretch_len=1,stretch_wid=5)

# ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx =0.75
Ball.dy =-0.75

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player "+Player_A+" : "+str(score_A)+"  Player "+Player_B+" : "+str(score_B),align="center",font=("Courier",24,"normal"))

#function
def paddle_A_up():
    y = paddle_A.ycor()
    y+=10
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y-=10
    paddle_A.sety(y)

def paddle_B_up():
    y = paddle_B.ycor()
    y+=10
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y-=10
    paddle_B.sety(y)

def exit():
    wn.bye()


#keyboard binding
wn.listen()
wn.onkeypress(paddle_A_up,"w")
wn.onkeypress(paddle_A_down,"s")
wn.onkeypress(paddle_B_up,"Up")
wn.onkeypress(paddle_B_down,"Down")


Play = True
# main game loop
while Play:

    wn.update()
    # move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # border Checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    elif Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    elif Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_A +=1
        # a+= 0.1
        # paddle_A.speed(a)
        pen.clear()
        pen.write("Player "+Player_A+" : " + str(score_A) + "  Player "+Player_B+" : " + str(score_B), align="center",
                  font=("Courier", 24, "normal"))

    elif Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx *= -1
        score_B +=1
        # a += 0.1
        # paddle_B.speed(a)
        pen.clear()
        pen.write("Player "+Player_A+" : " + str(score_A) + "  Player "+Player_B+" : " + str(score_B), align="center",
                  font=("Courier", 24, "normal"))

# paddle and ball collision
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and(Ball.ycor() < paddle_B.ycor()+40 and Ball.ycor() > paddle_B.ycor()-50):
        Ball.setx(340)
        Ball.dx*=-1
        # b +=0.2
        # Ball.speed(b)
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddle_A.ycor()+40 and Ball.ycor() > paddle_A.ycor()-50):
        Ball.setx(-340)
        Ball.dx *= -1
        # b += 0.2
        # Ball.speed(b)
        winsound.PlaySound("Bounce.wav", winsound.SND_ASYNC)

    if score_A == 10 or score_B == 10 :
        Play = False

wn.clear()
wn.bgcolor("black")
while True :
    if score_A > score_B :
        pen.goto(0, 0)
        pen.write("Player "+Player_A+" Win", align="center",font=("Courier", 24, "normal"))
        pen.goto(0, -260)
        pen.write("press space to exit the game", align="center", font=("Courier", 24, "normal"))
        wn.onkeypress(exit, "space")
    else :
        pen.goto(0, 0)
        pen.write("Player "+Player_B+" Win", align="center", font=("Courier", 24, "normal"))
        pen.goto(0, -260)
        pen.write("press space to exit the game", align="center", font=("Courier", 24, "normal"))
        wn.onkeypress(exit, "space")




