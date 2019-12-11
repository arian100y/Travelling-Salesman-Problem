from operator import itemgetter
import statistics
import time as ti

timer = ti.clock()
def dbToList(filename):
    arr = []
    file = open(filename,"r")

    for i in file:
        x = i.split(",")
        arr.append((float(x[0]),float(x[1])))

    return arr


def CrearCaminosGraf(quadrant, filename2):
    file2 = open(filename2, "w")
    n = len(quadrant)
    c = 0

    for u in quadrant:
        s2 = ""
        s2 += str(u[0]) + "," + str(u[1]) + " "
        cercanos = []
        for j in range(1, int(len(quadrant)/2)+1):
            v1 = (c + j) % len(quadrant)
            v2 = (c - j) % len(quadrant)

            xv1, yv1 = quadrant[v1][0], quadrant[v1][1]
            d1 = ((xv1 - u[0]) ** 2 + (yv1 - u[1]) ** 2) ** 0.5
            xv2, yv2 = quadrant[v2][0], quadrant[v2][1]
            d2 = ((xv2 - u[0]) ** 2 + (yv2 - u[1]) ** 2) ** 0.5
            if [v1, xv1, yv1, d1] not in cercanos :
                cercanos.append([v1, xv1, yv1, d1])
            if [v2, xv2, yv2, d2] not in cercanos:
                cercanos.append([v2, xv2, yv2, d2])
        cercanos.sort(key=itemgetter(3))

        for j in cercanos[:10]:
            s2 += str(j[1]) + "," + str(j[2]) + " "
        file2.write(s2[:-1] + "\n")
        p = n // 2

        c += 1

def separateLists(auxArr):
    yArr = []
    for i in auxArr:
        yArr += [i[1]]

    xArr = []
    aux = auxArr[:]
    aux.sort(key=itemgetter(0))
    for i in aux:
        xArr += [i[0]]
    return xArr,yArr


def CreateQuadrants(arr):
    xArr,yArr = separateLists(arr)
    yMedian = statistics.median(yArr)
    xMedian = statistics.median(xArr)
    print(xMedian,yMedian)
    q1,q2,q3,q4 = [],[],[],[]

    for i in arr:
        if i[0]<= xMedian and i[1] >= yMedian:
            q1 += [i]
        if i[0]> xMedian and i[1] >= yMedian:
            q2 += [i]
        if i[0]<= xMedian and i[1] < yMedian:
            q3 += [i]
        if i[0]> xMedian and i[1] < yMedian:
            q4 += [i]

    return q1,q2,q3,q4,xMedian,yMedian







