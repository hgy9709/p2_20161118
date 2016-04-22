import turtle
wn=turtle.Screen()
d1=turtle.Turtle()
wn.bgcolor("Lightyellow")
size=90

def Triangle():
 d1.penup()
 d1.goto(0,0)
 d1.pendown()
 for i in range(0,3):
  d1.fd(100)
  d1.right(120)
  d1.write("come in")

def Triangle2():
 d1.penup()
 d1.goto(-200,0)
 d1.pendown()
 d1.write("go")
 for i in range(0,3):
  d1.fd(100)
  d1.right(120)

def Circle1():
 d1.penup()
 d1.goto(200,100)
 d1.pendown()
 d1.write("go")
 d1.circle(65)

def Square():
 d1.penup()
 d1.goto(-200,280)
 d1.pendown()
 d1.write("go")
 for i in range(0,4):
  d1.fd(180)
  d1.right(90)

def Circle2():
 d1.penup()
 d1.goto(250,-200)
 d1.pendown()
 d1.write("go")
 d1.circle(90)

  

Triangle()
Triangle2()
Circle1()
Circle2()
Square()

d1.penup()




from turtle import *

move = Turtle()
move.shape("turtle")
showturtle()
move.penup()

def k1():
    move.forward(45)

def k2():
    move.left(45)

def k3():
    move.right(45)

def k4():
    move.back(45)


onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

listen()
mainloop()
