sentence="Sangmyung Univ., Hongji-dong, Jongno-gu, Seoul, Korea"
allchars=list(sentence)
    
d=dict()
for c in allchars:
    if c not in d:
        d[c]=1
    else:
        d[c]=d[c]+1

%matplotlib
import matplotlib
import matplotlib.pyplot as plt

plt.bar(range(len(d)),d.values(), align='center')
plt.xticks(range(len(d)), list(d.keys()))
plt.show()