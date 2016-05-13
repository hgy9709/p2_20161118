def Survey(): 
    Data_Satisfaction=[ 
        [13.1, 37.1], 
        [10.6, 34.6], 
        [27.1, 40.0], 
        [16.2, 37.8], 
        [11.4, 29.8], 
        [12.2, 26.5], 
        [13.5, 29.7], 
        [13.7, 37.6]] 
    Data_unSatisfaction=[ 
        [8.7, 1.5], 
        [13.4, 1.9], 
        [2.9, 1.5], 
        [6.8, 0.8], 
        [14.8, 4.9], 
        [14.9, 4.4], 
        [11.1, 2.4], 
        [4.1, 1.2]] 

 
    sum_Satisfaction=0 
    sum_unSatisfaction=0 
 
    for i in Data_Satisfaction: 
        sum_Satisfaction=i[0]+i[1] 
 
    for e in Data_unSatisfaction: 
        sum_unSatisfaction=e[0]+e[1] 
 

    print "sum of Satisfaction :",sum_Satisfaction
    print "sum of Unsatisfaction :",sum_unSatisfaction 
    print "average of Satisfaction :",float(sum_Satisfaction/len(Data_Satisfaction)) 
    print "average of Satisfaction :",float(sum_unSatisfaction/len(Data_unSatisfaction)) 

 
def lab11_2(): 
    Survey() 

def main():  
    lab11_2() 
 
if __name__=="__main__": 
    main() 
 
input() 