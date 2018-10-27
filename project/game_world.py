
# layer 0: Background Objects
# layer 1: player Objects
# layer 2: enemy Objects
# layer 3: item Objects
# layer 4: playerBullet Objects
# layer 5: Boom Objects
# layer 6: enemyBullet Objects

objects = [[],[],[],[],[],[]]


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

def clear():
    for o in all_objects():
        del o
    objects.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o
