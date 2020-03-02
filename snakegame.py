import turtle
from time import sleep
import random


# Set up the screen

wn = turtle.Screen()
wn.title("Snake game by @basantashahh")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) # this turns off the screen update

# lets create snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# creating sanke food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# create function
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




# creating function
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

# keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# lets create main game loop which keeps running
while True:
    wn.update()
    if head.distance(food) < 20:
        # move the food to random screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
    sleep(0.2)
    move()



wn.mainloop()