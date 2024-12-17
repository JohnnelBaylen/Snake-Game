import turtle
import time 
import random

delay = 0.1

Score = 0
HighScore = 0

screen = turtle.Screen()
screen.title("Crafted and Developed by @jthrone")
screen.bgcolor("green")
screen.setup(width=600, height=600)
screen.tracer(0)

# head snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

# food 
meal = turtle.Turtle()
meal.speed(0)
meal.shape("square")
meal.color("red")
meal.penup()
meal.goto(0,100)

sizes = []

# score label
score = turtle.Turtle()
score.speed(0)
score.shape("circle")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Score : 0  High Score : 0", align="center", font=("Times New Roman", 24, "normal"))


def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"    

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def function():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20) 

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20) 
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x + 20) 

    if head.direction == "right":
        x = head.xcor()
        head.setx(x - 20) 

screen.listen()
screen.onkeypress(goup, "w")
screen.onkeypress(godown, "s")
screen.onkeypress(goleft, "d")
screen.onkeypress(goright, "a")


# game loop 
while True:

    screen.update()

    # border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # hide size
        for size in sizes:
            size.goto(1000, 1000)
             
        # clear size
        sizes.clear()

        # reset the score
        Score = 0
        
        # reset the delay 
        delay = 0.1

        score.clear()
        score.write("Score : {}  "  "  High Score : {}".format(Score, HighScore), align="center", font=("Times New Roamn", 24, "normal"))
    
    # food
    if head.distance(meal) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        meal.goto(x,y)
        
        # Add Size
        nsize = turtle.Turtle()
        nsize.speed(0)
        nsize.shape("circle")
        nsize.color("yellow")
        nsize.penup()
        sizes.append(nsize)  

        # Add score 
        Score +=10

        if Score > HighScore:
            HighScore = Score

        score.clear()
        score.write("Score : {}  "  "  High Score : {}".format(Score, HighScore), align="center", font=("Times New Roamn", 24, "normal"))


    # Movement
    for index in range(len(sizes)-1, 0, -1):
        x = sizes[index-1].xcor()
        y = sizes[index-1].ycor()
        sizes[index].goto(x,y)
    if len(sizes) > 0:
        x = head.xcor()
        y = head.ycor()
        sizes[0].goto(x,y)

    function()

    # collision by self 

    for size in sizes:
        if size.distance(head) < 20:
            time.sleep(1)
            head.direction = "stop"

            # hide size
            for size in sizes:
                size.goto(1000, 1000)

            # clear size
            sizes.clear()


             # reset the score
            Score = 0

            # reset the delay
            delay = 0.1

            score.clear()
            score.write("Score : {}  "  "  High Score : {}".format(Score, HighScore), align="center", font=("Times New Roamn", 24, "normal"))

    time.sleep(delay)

