"""
@author 하근영
@since 0407
"""
def year():

    year=input("input the year")


    if(year%4==0) and (year%100!=0 or year%400==0):
        print"leap year"
    else:
        print"Not leap year"
year()

wn.exitonclick()

"""
repeat
start
:user input year;
if(year%4==0)and(year%100!=0 or year%400==0)
:print leap year;
else(no)
:print not leap lear;
endif
stop

def main():
     year()

"""

def updown():  
   import random  
   ai = input("Select your Max range  ")  
   r1 = random.randrange(1,ai+1)  
   global pl  
   print "Start Game!"  

  
  def game():  
      pl = input("Think your numbers!  ")  
      if (r1<pl):  
          result = "Down"  
          print result  
          game()  
      elif (r1>pl):  
          result = "UP"  
          print result  
          game()  
      else :  
          result = "Yes"  
          print result  
           if (result=="Yes"):  
              wn = raw_input("Good  ")  
  game() 

""" 

"""

start
Player : Select max range;  
Computer AI : Select random one number in range;  
Start Game!;  
Player input one number;   
while(Play)  
if (Compare Player N & AI N) then (Plater N < AI N)  
Up;  
else (Player N > AI B)  
Down;  
endif  
endwhile  
Player N = AI N;  
"Good";  
End Game;  
stop  

"""