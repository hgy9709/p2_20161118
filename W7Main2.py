import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 
mytracks=list()
mytracks.append(t1.pos())
t1.speed(1)
t1.penup() 
t1.goto(-400,300) 
t1.pendown() 
t1.pencolor("Red") 
t1.right(90) 
t1.fd(400)
mytracks.append(t1.pos())
t1.backward(150) 
mytracks.append(t1.pos())
t1.left(90) 
t1.fd(300) 
mytracks.append(t1.pos())
t1.left(90) 
t1.fd(300) 
mytracks.append(t1.pos())
t1.back(150) 
mytracks.append(t1.pos())
t1.right(90) 
t1.fd(300) 
mytracks.append(t1.pos())
t1.left(90) 
t1.right(90) 
t1.right(90) 
t1.fd(200) 
mytracks.append(t1.pos())
t1.fd(300) 
mytracks.append(t1.pos())
t1.back(100) 
mytracks.append(t1.pos())
t1.left(90) 
t1.fd(200) 
mytracks.append(t1.pos())
print mytracks
for t in range(0,len(mytracks)):
    print mytracks[t]
for t in mytracks:
    print t
def replaytracks(mytracks):
    for i in mytracks:
        t1.goto(mytrack[i])
    
def lab7():
    replayTracks()
    
def main():
    lab7

main()