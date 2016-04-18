def drawSquareAt(size,pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size) 
        t1.right(90)
    return tracks

def lab7a():
    size=100
    pos=t1.pos
    mytrack=drawSquareAt(size, pos)
    print mytrack
    
tracks=dict()
tracks=({1:(200,0),2:(200,200),3:(0,200),4:(0,0)})
def drawSquareFrom():
 for i in range(1,5):
  t1.goto(tracks[i])
  
def lab7b():
t1.penup()
t1.goto(0,0)
t1.pendown()
drawSquareFrom()

def main():
    lab7a()
    lab7b()
    
main()
wn.exitonclick()
