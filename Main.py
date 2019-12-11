from math import *
import heapq as hq
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

db= dbToList("testSet4.txt")
q1,q2,q3,q4,xMedian,yMedian = CreateQuadrants(db)
CrearCaminosGraf(q1,"Q1CaminosSet4.txt")
CrearCaminosGraf(q2,"Q2CaminosSet4.txt")
CrearCaminosGraf(q3,"Q3CaminosSet4.txt")
CrearCaminosGraf(q4,"Q4CaminosSet4.txt")
q1Com = generateWeightGraph(q1,"Q1CaminosSet4.txt")
q2Com = generateWeightGraph(q2,"Q2CaminosSet4.txt")
q3Com = generateWeightGraph(q3,"Q3CaminosSet4.txt")
q4Com = generateWeightGraph(q4,"Q4CaminosSet4.txt")


def makeSets(i):
    if(i is 2):
        db = dbToList("testSet4.txt")
        q1, q2, q3, q4, xMedian, yMedian = CreateQuadrants(db)
        CrearCaminosGraf(q1, "Q1CaminosSet4.txt")
        CrearCaminosGraf(q2, "Q2CaminosSet4.txt")
        CrearCaminosGraf(q3, "Q3CaminosSet4.txt")
        CrearCaminosGraf(q4, "Q4CaminosSet4.txt")
        q1Com = generateWeightGraph(q1, "Q1CaminosSet4.txt")
        q2Com = generateWeightGraph(q2, "Q2CaminosSet4.txt")
        q3Com = generateWeightGraph(q3, "Q3CaminosSet4.txt")
        q4Com = generateWeightGraph(q4, "Q4CaminosSet4.txt")
        return db,q1,q2,q3,q4,q1Com,q2Com,q3Com,q4Com
    if( i is 3):
        db = dbToList("testSet3.txt")
        q1, q2, q3, q4, xMedian, yMedian = CreateQuadrants(db)
        CrearCaminosGraf(q1, "Q1CaminosSet3.txt")
        CrearCaminosGraf(q2, "Q2CaminosSet3.txt")
        CrearCaminosGraf(q3, "Q3CaminosSet3.txt")
        CrearCaminosGraf(q4, "Q4CaminosSet3.txt")
        q1Com = generateWeightGraph(q1, "Q1CaminosSet3.txt")
        q2Com = generateWeightGraph(q2, "Q2CaminosSet3.txt")
        q3Com = generateWeightGraph(q3, "Q3CaminosSet3.txt")
        q4Com = generateWeightGraph(q4, "Q4CaminosSet3.txt")
        return db, q1, q2, q3, q4, q1Com, q2Com, q3Com, q4Com

global t
t = []
global qCoords
qCoords = []

def check(visi,e):
    for i in range(len(visi)):
        if visi[i] == False and i!= e:
            return False
    return True

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
qCoords = []

start1, end1 = furthestPoints(q1,1)
qCoords += [[(q1[start1]),(q1[end1])]]
start3, end3 = furthestPoints(q3,3)
qCoords += [[(q3[start3]),(q3[end3])]]
start4, end4 = furthestPoints(q4,4)
qCoords += [[(q4[start4]),(q4[end4])]]
start2, end2 = furthestPoints(q2,2)
qCoords += [[(q2[start2]),(q2[end2])]]


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


def find(s, a):
    if s[a] < 0:
        return a
    else:
        granpa = find(s, s[a])
        s[a] = granpa
        return granpa
def union(s, a, b):
    pa = find(s, a)
    pb = find(s, b)
    if pa == pb: return
    if s[pa] <= s[pb]:
        s[pa] += s[pb]
        s[pb] = pa
    elif s[pb] < s[pa]:
        s[pb] += s[pa]
        s[pa] = pb
def ordenarAristas(G):
    cola = []
    for u in range(len(G)):
        for v, w in G[u]:
            hq.heappush(cola, (w, u, v))
    return cola
def Kruskal(G):
    cola = ordenarAristas(G)
    n = len(G)
    raices = [-1] * n
    T = []
    while len(cola) > 0:
        w, u, v = hq.heappop(cola)

        if find(raices, u) != find(raices, v):


            union(raices, u, v)
            T.append((u, v, w))

    return T



def makeTree(T, graph,end):
    tree = [[] for i in range(len(graph))]
    for i in range(len(graph)):
        for j in T:
            if(j[0] == i):
                tree[i] += [(j[1],j[2])]

    if (len(tree[end]) > 0):
        for v, w in tree[end]:
            tree[v] += [(end, w)]
        tree[end] = []
    return tree

def findDistance(v,u,i):
    if(i == 1):
        x1,y1 = q1[v]
        x2,y2 = q1[u]
        distance = sqrt((x2 - x1) ** 2 + (x2 - x1) ** 2)
    if (i == 2):
        x1, y1 = q2[v]
        x2, y2 = q2[u]
        distance = sqrt((x2 - x1) ** 2 + (x2 - x1) ** 2)
    if (i == 3):
        x1, y1 = q3[v]
        x2, y2 = q3[u]
        distance = sqrt((x2 - x1) ** 2 + (x2 - x1) ** 2)
    if (i == 4):
        x1, y1 = q4[v]
        x2, y2 = q4[u]
        distance = sqrt((x2 - x1) ** 2 + (x2 - x1) ** 2)
    return distance

def OPT(tree,start,end,q):
    visited = [False] * len(tree)
    order = []
    node = start
    recorrido = []

    while(False in visited):


        if(visited[node]== False and node != end ):
            order = []
            visited[node] = True

            for v,w in tree[node]:
                hq.heappush(order,(w,v))

            if(len(order) > 0):
                w,v = hq.heappop(order)
                if( v == end ):
                        if(len(order)>0):

                            w2,v2 = hq.heappop(order)
                            hq.heappush(order,(w,v))
                            w,v = w2,v2
                        else:
                            for i in range(len(tree)):
                                if (i != end and visited[i] == False):

                                    v = i
                                    break

                elif(visited[v]==True ):
                    if (len(order) > 0):
                        w2, v2 = hq.heappop(order)
                        hq.heappush(order, (w, v))
                        w, v = w2, v2
                    else:
                        for i in range(len(tree)):
                            if (i != end and visited[i] == False):
                                v = i
                                break
                if(check(visited,end) == True):
                    v = end
                findDistance(node, v,q)
                recorrido.append((node,v , w))

                for m in range(len(order)): #inherit nodes
                    w1,v1 = hq.heappop(order)
                    tree[v] += [(v1,findDistance(v,v1,q))]
                node = v

        elif check(visited,end)==False:
            for i in range(len(tree)):
                if(i != end and visited[i] == False):
                    recorrido.append((node,i,findDistance(node,i,q)))
                    node = i
                    break
        elif check(visited,end):
            visited[end] = True

    return recorrido




def finalAlgorithm(i):


    makeSets(i)

    MST1 = Kruskal(q1Com)
    MST2 = Kruskal(q2Com)
    MST3 = Kruskal(q3Com)
    MST4 = Kruskal(q4Com)
    t1 = makeTree(MST1, q1Com, end1)
    t2 = makeTree(MST2, q2Com, end2)
    t3 = makeTree(MST3, q3Com, end3)
    t4 = makeTree(MST4, q4Com, end4)

    r1 = OPT(t1,start1,end1,1)
    print(r1)
    print()
    print(start3,"end",end3)
    r3 = OPT(t3, start3, end3,3)
    print(r3)
    print()
    print(start4, "end", end4, "len ", len(t4))
    r4 = OPT(t4, start4, end4,4)
    print(r4)


    print()

    print(start2, "end", end2, "len ", len(t2))
    r2 = OPT(t2, start2, end2,2)
    r2 = r2[:-1]
    print(r2)
    print()
    recorrido = join(r1,r2,r3,r4)


    cost = 0

    for i in recorrido:
        cost += i[2]
    time = ti.clock() - timer
    print("cost/distancia:", cost)


    return recorrido,time,cost


reco,time,cost = finalAlgorithm(1)

