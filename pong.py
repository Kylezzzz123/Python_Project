import turtle   # turtle is a module to do some basic graphics
import winsound

wn = turtle.Screen()       # to show a screen
wn.title("Pong by Kyze")
wn.bgcolor("black")        # background color
wn.size(width=800, height=600)
wn.tracer(0)               # tracer(0) is to stop the window from updating, speed up the game

#Score
score_a = 0
score_b = 0 


#Paddle A (object A)
paddle_a = turtle.Turtle()         # turtle is module name from import, Turtle() is class name
paddle_a.speed(0)                  # this is speed of animation, set the speed to the maximum possible speed
paddle_a.shape("square")           # set shape of object
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)   # change the width and length of the object
paddle_a.penup()                   # draw a line as it is moving, but here penup(), we don't need to draw a line
paddle_a.goto(-600,0)              # goto(x,y)

#Paddle B (object B)
paddle_b = turtle.Turtle()         # turtle is module name from import, Turtle() is class name
paddle_b.speed(0)                  # this is speed of animation, set the speed to the maximum possible speed
paddle_b.shape("square")           # set shape of object
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)   # change the width and length of the object
paddle_b.penup()                   # draw a line as it is moving, but here penup(), we don't need to draw a line
paddle_b.goto(+600,0)              # goto(x,y)

#Ball
ball = turtle.Turtle()         # turtle is module name from import, Turtle() is class name
ball.speed(0)                  # this is speed of animation, set the speed to the maximum possible speed
ball.shape("square")           # set shape of object
ball.color("white")
ball.penup()                   # draw a line as it is moving, but here penup(), we don't need to draw a line
ball.goto(0,0)              # goto(x,y)
ball.dx = -0.2                    # "d" is delta or change, everytime the ball moves, since x is positive, it moves to the right 2
ball.dy = 0.2                 # "d" is delta or change, everytime the ball moves, since y is positive, it moves to the up 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()            # We hide the pen
pen.goto(0,+350)
pen.write("Player A: 0   Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor()        # paddle_a is name of object A, ycor() is from turtle module, it means to retrun y coordinate
    y += 20
    paddle_a.sety(y)           # set the y to the new paddle to new y coordinate
    
def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)    

def paddle_b_up():
    y = paddle_b.ycor()        # paddle_a is name of object A, ycor() is from turtle module, it means to retrun y coordinate
    y += 20
    paddle_b.sety(y)           # set the y to the new paddle to new y coordinate
    
def paddle_b_down():
    y = paddle_b.ycor()
    y-= 20
    paddle_b.sety(y) 

# Keyboard binding
wn.listen()                       # lisen for keyboard input
wn.onkeypress(paddle_a_up, "w")   # when user press "w", call the function "paddle_a_up"
wn.onkeypress(paddle_a_down, "s") # when user press "s", call the function "paddle_a_up"
wn.onkeypress(paddle_b_up, "Up") # when user press "s", call the function "paddle_a_up"
wn.onkeypress(paddle_b_down, "Down") # when user press "s", call the function "paddle_a_up"

# Main game loop
while True:
    wn.update()             #everytime the loop run, it updates the screen
     
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)                    # setx(ball.xcor()) is current x corrdinate
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 390:
       ball.sety(390)
       ball.dy *= -1       # when the ball hits to 290, it Moves back to negative 1 (-1)
       winsound.PlaySound("ball.wav", winsound.SND_ASYNC)
       
     
    if ball.ycor() < -390:
       ball.sety(-390)
       ball.dy *= -1       # when the ball hits to 290, it Moves back to negative 0.1 (-0.1)
       winsound.PlaySound("ball.wav", winsound.SND_ASYNC)

    if ball.xcor() > 650: 
       ball.goto(0,0)      # go back to original 0,0
       ball.dx *= -1
       score_a += 1
       pen.clear()
       pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))           # " {} {} {} ".format(x,y,z), x to first {}, y for second {}, z for third {]}

    if ball.xcor() < -650: 
       ball.goto(0,0)
       ball.dx *= -1
       score_b += 1
       pen.clear()
       pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))           # " {} {} {} ".format(x,y,z), x to first {}, y for second {}, z for third {]}


    # Paddle and ball  collisions
    if (ball.xcor() > 590 and ball.xcor() < 610) and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40:    
        ball.setx(590)
        ball.dx *= -1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC)
               
    if (ball.xcor() < -590 and ball.xcor() > -610) and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40:
        ball.setx(-590)
        ball.dx *= -1
        winsound.PlaySound("ball.wav", winsound.SND_ASYNC)