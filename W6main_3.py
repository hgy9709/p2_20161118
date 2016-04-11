x=list()
def sumList(x):
        for i in range(0,1001):
                if(i%4==0 and i%5>0):
                        x.append(i)
        sum=0
        for g in range(0,len(x)):
                sum=sum+x[g]
        return sum
        print sum
def lab6():
        print sumList(x)
lab6()

def main():
    lab6()