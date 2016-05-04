import math
Locations=tuple()
MyList=list()
(x1,y1)=(37.571779, 126.976473)
Locations=[(37.570434, 126.983136), (37.579849, 126.977069), (37.574799, 126.957859), (37.565858, 126.976912), (37.570704, 126.992223)]
for i in Locations:
    MyList.append (math.sqrt((x1-i[0])**2+(y1-i[1])**2))
print min(MyList)