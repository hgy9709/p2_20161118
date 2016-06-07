import turtle 
import math 
import time 
wn=turtle.Screen() 
t1=turtle.Turtle() 
t2=turtle.Turtle() 
t2.shape("turtle") 
t2.color("red") 
t2.penup() 
t2.goto(0,-300) 
t2.setheading(90) 
t1.speed(20) 
wn.bgcolor("lightblue") 
wn.setup(600,400) 
result=0 
 
def OpenCoords(): 
    filehome=open('position.txt') 
    coords=list()
    for line in filehome: 
        cirpos=line.split(',') 
        coords.append([cirpos[0],cirpos[1], cirpos[2],cirpos[3], cirpos[4],cirpos[5].strip()]) 
    filehome.close() 
    return coords 
coords=OpenCoords() 
 
 
   
	 

def square1(): 
    for coord in coords: 
        x1=int(coords[0][0]) 
        x2=int(coords[0][1]) 
        y1=int(coords[0][2]) 
        y2=int(coords[0][3]) 
        x3=int(coords[0][4]) 
        y3=int(coords[0][5]) 

    t1.penup() 
    t1.goto(x1,y1)
    t1.pendown()
    t1.fillcolor("pink")
    t1.begin_fill() 
    for i in range(0,4): 
        t1.fd(100) 
        t1.right(90) 

    t1.end_fill() 
 
 
def square3(): 
    for coord in coords: 
        x1=int(coords[0][0]) 
        x2=int(coords[0][1]) 
        y1=int(coords[0][2]) 
        y2=int(coords[0][3]) 
        x3=int(coords[0][4]) 
        y3=int(coords[0][5]) 

    t1.penup() 
    t1.goto(x3,y3)
    t1.pendown()
    t1.fillcolor("black")
    t1.begin_fill() 
    for i in range(0,4): 
        t1.fd(100) 
        t1.right(90) 

    t1.end_fill() 
         
         
def square2(): 
    for coord in coords: 
        x1=int(coords[0][0]) 
        x2=int(coords[0][1]) 
        y1=int(coords[0][2]) 
        y2=int(coords[0][3]) 
        x3=int(coords[0][4]) 
        y3=int(coords[0][5]) 
            
    t1.penup() 
    t1.goto(x2,y2)
    t1.pendown()
    t1.fillcolor("blue")
    t1.begin_fill() 
    for i in range(0,4): 
        t1.fd(100) 
        t1.right(90) 

    t1.end_fill() 


                 
def do(): 
    square1() 
    square2() 
    square3() 

def squarein(): 
    (x,y)=t2.pos() 
    global result 
    if -200<=x<-100 and 180<=y<=280: 
        result=result+1 
        print(" point %d " % result) 
        t2.goto(0,-200) 
 

def squarein3(): 
    (x,y)=t2.pos() 
    global result 
    if 250<=x<350 and -200<=y<=-100: 
        result=result+1 
        print(" point %d " % result) 
        t2.goto(0,-200)  
 
 

def squarein2(): 
    (x,y)=t2.pos() 
    global result 
    if -250<=x<-150 and -350<=y<=-250: 
        result=result+1 
        print(" point %d " % result) 
        t2.goto(0,-200)


 
     
do() 
    

      

      
     
      
def k1(): 
    t2.forward(20) 
    squarein() 
    squarein2() 
    squarein3()
    squarein4() 
     
           
def k2(): 
    t2.left(45) 
 
def k3(): 
    t2.right(45) 
 
def k4(): 
    t2.back(30)   
   
wn.onkey(k1, "Up") 
wn.onkey(k2, "Left") 
wn.onkey(k3, "Right") 
wn.onkey(k4, "Down") 
wn.listen() 
  
turtle.mainloop() 
