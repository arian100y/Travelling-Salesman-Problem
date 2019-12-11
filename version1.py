from math import *
import heapq as pq
import time
from createCaminos import *
graph = []

def generateWeightGraph(graph,filename):
    text = open(filename, "r")
    graphh = []
    for i in text:
        aux = i.split(" ")
        test = []
        auxCoord = aux[0].split(",")
        auxX, auxY = float(auxCoord[0]), float(auxCoord[1])
        c = 0
        for j in aux:
                coord = j.split(",")
                x,y = float(coord[0]),float(coord[1])
                distance = sqrt((auxX - x)**2+(auxY - y)**2)
                idx = graph.index((x,y))

                if c!= 0:
                    test += [(idx,distance)]
                #else : test += [(x,y)]
                c+=1

        graphh += [test]

    return graphh

db= dbToList("testSet2.txt")

q1,q2,q3,q4,xMedian,yMedian = CreateQuadrants(db)
def furthestPoints(quadrant,num):
    x= quadrant[0][0]
    y = quadrant[0][1]
    start,end = 0,0
    for i in range(1,len(quadrant)):
        if num == 1:
            if quadrant[i][0] > x:
                x =quadrant[i][0]
                start = i
        if num == 2:
            length = sqrt((qCoords[2][1][0] - x) ** 2 + (qCoords[2][1][1] - y) ** 2)
            auxLength = sqrt((qCoords[2][1][0] - quadrant[i][0]) ** 2 + (qCoords[2][1][1] - quadrant[i][1]) ** 2)
            if (auxLength < length ) :
                length = auxLength
                x = quadrant[i][0]
                y = quadrant[i][1]
                start = i
        if num == 3:
            length = sqrt((qCoords[0][1][0] - x) ** 2 + (qCoords[0][1][1] - y) ** 2)
            auxLength = sqrt((qCoords[0][1][0] - quadrant[i][0]) ** 2 + (qCoords[0][1][1] - quadrant[i][1]) ** 2)
            if (auxLength < length):
                length = auxLength
                x = quadrant[i][0]
                y = quadrant[i][1]
                start = i

        if num == 4:
            length = sqrt((qCoords[1][1][0] - x) ** 2 + (qCoords[1][1][1] - y) ** 2)
            auxLength = sqrt((qCoords[1][1][0] - quadrant[i][0]) ** 2 + (qCoords[1][1][1] - quadrant[i][1]) ** 2)
            if (auxLength < length):
                length = auxLength
                x = quadrant[i][0]
                y = quadrant[i][1]
                start = i
    x = quadrant[0][0]
    y = quadrant[0][1]

    for i in range(1, len(quadrant)):
        if num == 1:
            if quadrant[i][1] < y and i != start :
                y =quadrant[i][1]
                end = i
        if num == 2:
            length = sqrt((qCoords[0][0][0] - x) ** 2 + (qCoords[0][0][1] - y) ** 2)
            auxLength = sqrt((qCoords[0][0][0] - quadrant[i][0] ) ** 2 + (qCoords[0][0][1] - quadrant[i][1]) ** 2)
            if (auxLength < length and i != start)  :
                length = auxLength
                x=quadrant[i][0]
                y = quadrant[i][1]
                end = i
        if num == 3:
            if (quadrant[i][0] > x and i != start)or (quadrant[i][1] < y and i != start and quadrant[i][0] < x) :
                x =quadrant[i][0]
                end = i
        if num == 4:

            if (quadrant[i][1] > y and i != start) or (quadrant[i][1] < y and i != start and quadrant[i][0] > x) :
                y =quadrant[i][1]
                end = i



    return start,end


CrearCaminosGraf(q1,"Q1CaminosSet2.txt")
CrearCaminosGraf(q2,"Q2CaminosSet2.txt")
CrearCaminosGraf(q3,"Q3CaminosSet2.txt")
CrearCaminosGraf(q4,"Q4CaminosSet2.txt")

q1Com = generateWeightGraph(q1,"Q1CaminosSet2.txt")
q2Com = generateWeightGraph(q2,"Q2CaminosSet2.txt")
q3Com = generateWeightGraph(q3,"Q3CaminosSet2.txt")
q4Com = generateWeightGraph(q4,"Q4CaminosSet2.txt")


def check(visi,e):
    for i in range(len(visi)):
        if visi[i] == False and i!= e:
            return False
    return True


global t
t = []
global qCoords
qCoords = []

def DFSUtil(g, s, visitado,end):
    visitado[s[1]] = True
    queue = []
    for i in g[s[1]]:
        pq.heappush(queue,(i[1],i[0]))
    global counter
    print(s[1], end=" ")
    global t
    for x in queue:
        if (visitado[x[1]] == False and x[1] != end) or (len(g)== 2 and visitado[end] == False):

            t += [(s[1], x[1], x[0])]
            DFSUtil(g, x, visitado,end)
            return

def DFS(g, graphCoord,num):
    visitado = [False] * (len(g))
    global t
    t = []
    start, end = furthestPoints(graphCoord,num)
    print(start,end)
    global qCoords
    qCoords += [[(graphCoord[start]),(graphCoord[end])]]
    print("start:",start,"end:",end)
    while False in visitado:
        DFSUtil(g, (0, start), visitado,end)

        if  check(visitado,end) ==  False :

            for i in range(len(visitado)):
                if visitado[i] == False and i != end:
                    start = i

                    break

            x,y = graphCoord[start][0], graphCoord[start][1]
            auxX,auxY = graphCoord[t[-1][0]][0] ,graphCoord[t[-1][0]][1]
            weight =  sqrt((auxX - x)**2+(auxY - y)**2)

            t += [(t[-1][1], start, weight)]

        else :
            if(visitado[end]==False):
                i = len(t) - 1

                x, y = graphCoord[t[i][0]][0], graphCoord[t[i][0]][1]
                auxX, auxY = graphCoord[end][0], graphCoord[end][1]
                weight = sqrt((auxX - x) ** 2 + (auxY - y) ** 2)

                t += [(t[i][1], end, weight)]
                visitado[end] = True
                print(end)

    return t

def join(t1,t2,t3,t4):
    recorrido = []
    for j in t1:
        coord1 = q1[j[0]]
        coord2 = q1[j[1]]
        recorrido += [(db.index(coord1), db.index(coord2), j[2])]
    x1, y1 = q1[t1[-1][1]][0], q1[t1[-1][1]][1]
    x2, y2 = q3[t3[0][0]][0], q3[t3[0][0]][1]
    distance = sqrt((x2 - x1) ** 2 + (x2 - x1) ** 2)
    recorrido += [(db.index((x1, y1)), db.index((x2, y2)), distance)]
    for j in t3:
        coord1 = q3[j[0]]
        coord2 = q3[j[1]]
        recorrido += [(db.index(coord1), db.index(coord2), j[2])]
    x1, y1 = q3[t3[-1][1]][0], q3[t3[-1][1]][1]
    x2, y2 = q4[t4[0][0]][0], q4[t4[0][0]][1]
    distance = sqrt((x2 - x1) ** 2 + (x2 - x1) ** 2)
    recorrido += [(db.index((x1, y1)), db.index((x2, y2)), distance)]
    for j in t4:
        coord1 = q4[j[0]]
        coord2 = q4[j[1]]
        recorrido += [(db.index(coord1), db.index(coord2), j[2])]
    x1, y1 = q4[t4[-1][1]][0], q4[t4[-1][1]][1]
    x2, y2 = q2[t2[0][0]][0], q2[t2[0][0]][1]
    distance = sqrt((x2 - x1) ** 2 + (x2 - x1) ** 2)
    recorrido += [(db.index((x1, y1)), db.index((x2, y2)), distance)]
    for j in t2:
        coord1 = q2[j[0]]
        coord2 = q2[j[1]]
        recorrido += [(db.index(coord1), db.index(coord2), j[2])]
    x1, y1 = q2[t2[-1][1]][0], q2[t2[-1][1]][1]
    x2, y2 = q1[t1[0][0]][0], q1[t1[0][0]][1]

    distance = sqrt((x2 - x1) ** 2 + (x2 - x1) ** 2)
    recorrido += [(db.index((x1, y1)), db.index((x2, y2)), distance)]

    return recorrido

def makeFullGraph():
    weighedGraph = [[]] * len(db)
    c=0
    for i in q1Com:
        for j in i:
            coord = q1[c]
            index = db.index(q1[j[0]])
            weight = j[1]
            rIndex = db.index(coord)
            weighedGraph[rIndex] += [(index,weight)]
        c+= 1
    c = 0
    for i in q2Com:
        for j in i:

            coord = q2[c]
            index = db.index(q2[j[0]])
            weight = j[1]
            rIndex = db.index(coord)
            weighedGraph[rIndex] += [(index, weight)]
        c += 1
    c = 0
    for i in q3Com:
        for j in i:

            coord = q3[c]
            index = db.index(q3[j[0]])
            weight = j[1]
            rIndex = db.index(coord)
            weighedGraph[rIndex] += [(index, weight)]
        c += 1
    c = 0
    for i in q4Com:
        for j in i:

            coord = q4[c]
            index = db.index(q4[j[0]])
            weight = j[1]
            rIndex = db.index(coord)
            weighedGraph[rIndex] += [(index, weight)]
        c += 1

    return weighedGraph



def AlgoritmoFinal():

    t1 = DFS(q1Com,  q1,1)
    print()
    t3 = DFS(q3Com, q3, 3)
    print()
    t4 = DFS(q4Com, q4, 4)
    print()
    t2 = DFS(q2Com,  q2,2)
    print()
    print("--------")
    recorrido = join(t1,t2,t3,t4)
    print("recorrido:",recorrido)
    cost = 0

    for i in t1:
        cost += i[2]
    print("test",cost)
    cost = 0
    test = makeFullGraph()
    #print(test)
    for i in recorrido:
        cost += i[2]
    time = ti.clock() - timer
    print("cost/distancia:",cost)
    return recorrido,cost,time

reco,cost,time = AlgoritmoFinal()


