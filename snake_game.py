import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,0)
food.direction = "stop"

bodyparts = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#main game loop
while True:
    wn.update()

    #border touch
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for bodypart in bodyparts:
            bodypart.goto(1000,1000)

        bodyparts.clear()

        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
  
#food touch
    if head.distance(food) < 20:
        #move food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #add to body
        new_bodypart = turtle.Turtle()
        new_bodypart.speed(0)
        new_bodypart.shape("square")
        new_bodypart.color("purple")
        new_bodypart.penup()
        bodyparts.append(new_bodypart)

        #get faster
        delay -= 0.001

        #add to score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(bodyparts) -1, 0, -1):
        x = bodyparts[index-1].xcor()
        y = bodyparts[index-1].ycor()
        bodyparts[index].goto(x, y)

    if len(bodyparts) > 0:
        x = head.xcor()
        y = head.ycor()
        bodyparts[0].goto(x, y)

    move()

    for bodypart in bodyparts:
        if bodypart.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for bodypart in bodyparts:
                bodypart.goto(1000,1000)

            bodyparts.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()