sides=10

size=10

bigger=10

angle=90

import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

for i in range(0,sides):
    if(i%2):
        size=size+bigger
        



def makeSwirlSquare(size,bigger,turns,sides,angle):
    for i in range(sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(angle)
            

makeSwirlSquare(20,10,10,50,90)

wn.exitonclick()