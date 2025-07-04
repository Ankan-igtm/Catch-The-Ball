import turtle
import time
import random

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Catch The Ball by Ankan")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Bowl 
bowl = turtle.Turtle()
bowl.speed(0)
bowl.shape("square")
bowl.color("aqua")
bowl.shapesize(stretch_wid=1, stretch_len=4)  
bowl.penup()
bowl.goto(0, -250)
bowl.direction = "stop"

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(random.randint(-280, 280), 280)
ball.dy = -4  

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Move functions
def go_left():
    x = bowl.xcor()
    x -= 20
    if x < -280:
        x = -280
    bowl.setx(x)

def go_right():
    x = bowl.xcor()
    x += 20
    if x > 280:
        x = 280
    bowl.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_left, "n")
wn.onkeypress(go_right, "m")

# Main game loop
while True:
    wn.update()

    # Move ball down
    y = ball.ycor()
    y += ball.dy
    ball.sety(y)

    # Check for collision with bowl
    if ball.distance(bowl) < 50 and ball.ycor() < -230:
        score += 10
        ball.goto(random.randint(-280, 280), 280)
        ball.dy -= 0.1  
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    # Ball missed
    if ball.ycor() < -280:
        score = 0
        ball.goto(random.randint(-280, 280), 280)
        ball.dy = -3  

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    time.sleep(0.02)  