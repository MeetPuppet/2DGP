import pickle

# layer 0: Background Objects
# layer 1: Foreground Objects
objects = [[],[],[]]


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for l in objects:
        l.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

def comu():
    player = objects[1][0]
    zombies = objects[2]

    for zombie in zombies:
        if collide(player,zombie):
            return True
    return False

def save():
    # fill here
    with open('game.sav', 'wb') as f:
        pickle.dump(objects,f)
    pass

def load():
    # fill here
    global objects
    with open('game.sav', 'rb') as f:
        objects = pickle.load(f)
    pass
