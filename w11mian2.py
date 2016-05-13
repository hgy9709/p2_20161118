Martin = list() 
Hoover=list() 
Martin = [To the confidence and consolation derived from these sources it would be ungrateful not to add those which spring from our present fortunate condition.
Though not altogether exempt from embarrassments that disturb our tranquillity at home and threaten it abroad, yet in all the attributes of a great, happy, and flourishing people we stand without a parallel in the world
. Abroad we enjoy the respect and, with scarcely an exception, the friendship of every nation; at home, while our Government quietly but efficiently performs the sole legitimate end of political institutions--in doing the greatest good to the greatest number--we present an aggregate of human prosperity surely not elsewhere to be found.]
Hoover=[It detracts nothing from the character and energy of the American people, it minimizes in no degree the quality of their accomplishments to say that the policies of the Republican Party have played a large part in recuperation from the war and the building of the magnificent progress which shows upon every hand today. 
I say with emphasis that without the wise policies which the Republican Party has brought into action during this period, no such progress would have been possible.]
def countWords(doc): 
    d = dict() 
    for sentence in doc: 
        words=sentence.split() 
        for word in words: 
            if word in d: 
                d[word]+=1 
            else: 
                d[word]=1 
    return d 
 
def FrequentWordsList(c,d): 
    w=set() 
    for k in d: 
        if d[k]>c: 
            w.add(k) 
    return w 
 
def Only_(): 
    print "Only Martin words :",w_M.difference(w_M) 
    print "Only Hoover words :",w_H.difference(w_H) 
 
def Both():  
    print "Both Martin and Hoover :",w_M.intersection(w_H)  
def All():  
   print "ALL of Frequent words:",w_M.union(w_H)  
 

d_M=dict() 
d_H=dict() 
 
d_M=countWords(Martin) 
d_H=countWords(Hoover) 
    
w_M=set() 
w_H=set() 
 
w_M=FrequentWordsList(8,d_M) 
w_H=FrequentWordsList(23,d_H)     
           
def lab11_3():  
 
    # 단어 10개씩 찾기 

     print "Frequent words of Lincoln :",w_M 
    print "Frequent words of Bush :",w_H
    
    # 단어 비교하기 
 
    Only_() 
    Both() 
    All() 
      
def main():  
    lab11() 
  
if __name__=="__main__": 
    main()

 
input() 