import matplotlib.pyplot as plt
from UCS import *

x=[]
y=[]
for i in reco:
    x1=db[i[0]][0]
    y1 = db[i[0]][1]
    x += [x1]
    y+= [y1]

x += [x[0]]
y += [y[0]]



plt.plot(x,y)
plt.text(-84,-17.5,"Distancia: "+str(cost))
plt.text(-84,-19.5,"Tiempo: "+str(time))
plt.plot(x,y,'.')
plt.plot(x[0],y[0],'rx')
plt.axhline(yMedian, color='black')
plt.axvline(xMedian, color='black')
plt.show()

