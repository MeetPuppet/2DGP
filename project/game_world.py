
# layer 0: Background Objects
# layer 1: player Objects
# layer 2: enemy Objects
# layer 3: item Objects
# layer 4: playerBullet Objects
# layer 5: Boom Objects
# layer 6: enemyBullet Objects

objects = [[],[],[],[],[],[]]

import math
def getDistance(startPoint, endPoint):
    Xdistance = startPoint[0] - endPoint[0]
    Ydistance = startPoint[1] - endPoint[1]
    return math.sqrt(Xdistance**2+Ydistance**2)

def getAngle(startPoint, endPoint):

    Xdistance = endPoint[0] - startPoint[0]
    Ydistance = endPoint[1] - startPoint[1]
    distance = math.sqrt(Xdistance ** 2 + Ydistance ** 2)

    angle = math.acos(Xdistance / distance)

    if endPoint[1] > startPoint[1] :
        angle = (3.141592*2) - angle
        if angle > (3.141592*2):
            angle -= (3.141592*2)

    return angle

    pass


def add_object(o, layer):
    objects[layer].append(o)

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o


def remove_object2(o, num):
    if o in objects[num]:
        objects[num].remove(o)
        del o

def intersectAtoB(objectA, AList, objectB, BList):
    distance = None
    for A in range(len(objects[AList])):
        for B in range(len(objects[BList])):
            distance = getDistance(objectA.getPoint(), objectB.getPoint())
            #object마다 object.getRadius()가 필요함
            #hitRange = raidus1 + radius2
            '''
            하나가 지워지면 다른하나가 안지워질수 있음
            반대로 둘다 지워질 수도 있음
            '''
    pass

def clear():
    for o in all_objects():
        del o
    objects.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o
