class Dog(object): 
    def __init__(self,name): 
        self.name=name 
    def Name(self): 
        print 'my dog name ',self.name 
    def talk(self): 
        print 'dogs say : mung mung' 

class Shihtu(object): 
    def __init__(self,name): 
        self.name=name 
    def talk(self): 
        print 'ShihTzu : si si' 
 
class Maltse(object): 
    def __init__(self,name): 
        self.name=name 
    def talk(self): 
        print 'Maltese : mal mal' 
 
def DogsSay(): 
    mydog=Dog('dogs') 
    mydog.talk() 
    myshihtu=Shihtu('Shihtu') 
    myshihtu.talk() 
    mymaltse=Maltse('Maltse') 
    mymaltse.talk() 
 
def lab14(): 
    DogsSay() 
 
def main(): 
    lab14() 
 
if __name__=="__main__": 
 main()  
  