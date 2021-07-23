# Author : Prasanna Thalpati


##### Snake Game #####                      


#set screen
import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game created by PRASANNA")
wn.setup(width=600, height=600)
wn.bgcolor("blue")
wn.tracer(0) #turns off the screen update

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food 
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#pen (scoring)
pen = turtle.Turtle()
pen.color("white")
pen.shape("square")
pen.penup()
pen.speed(0)
pen.goto(0,260)
pen.hideturtle()
pen.write("Score : 0 High Score : 0", align="center", font=("courier",20,"normal"))


#Functions 

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

#keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#main game loop
while True:
    wn.update()

#collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

#hide the segments
        for segment in segments:
            segment.goto(1000,1000)

#clear the segments lists
        segments.clear()            
#Reset the Score
        score = 0
        pen.clear()
        pen.write("score : {}  High Score : {}".format(score, high_score), align="center",font=("courier",20,"normal"))
#Move a food to a random spot
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)        

#snake collision with food add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

#Increasing score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("score : {}  High Score : {}".format(score, high_score), align="center",font=("courier",20,"normal"))

#Move the end segments with the first 
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
        #Move segment 0 where the head is 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y) 


    move()
#head collision with the body (snake touches own body and die)  
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
#hide the segments
            for segment in segments:
                segment.goto(1000,1000)

#clear the segments lists
            segments.clear()                
    
    time.sleep(delay)
     


wn.mainloop() 