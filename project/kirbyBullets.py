from pico2d import *

class kirbyBullet1:
    image = None
    def __init__(self, point):
        self.x, self.y = point[0], point[1]
        self.size = 0
        self.damage = 1
        self.frame=0
        if kirbyBullet1.image == None:
            kirbyBullet1.image = load_image('image/kirby/kirbyBullet.png')
        pass
    def update(self):
        self.x += 35
        self.frame= (self.frame+1)%3



        pass
    def render(self):
        self.image.clip_draw(self.frame*72,0,72,10,self.x,self.y)
        pass


    def getX(self): return self.x
    def getKind(self): return self.size
    def getDamage(self): return self.damage
    pass
class kirbyBullet2:
    image = None
    def __init__(self, point):
        self.x, self.y = point[0], point[1]
        self.size = 1
        self.damage = 4
        self.frame=0
        if kirbyBullet2.image == None:
            kirbyBullet2.image = load_image('image/kirby/kirbyBullet2.png')
        pass
    def update(self):
        self.x += 50
        self.frame= (self.frame+1)%6
        pass
    def render(self):
        self.image.clip_draw(self.frame*126,0,126,48,self.x,self.y)
        pass


    def getX(self): return self.x
    def getKind(self): return self.size
    def getDamage(self): return self.damage
    pass

class maxBullet:
    image = None
    def __init__(self, point):
        self.x, self.y = point[0], point[1]
        self.size = 2
        self.frame=0
        self.damage = 10
        if maxBullet.image == None:
            maxBullet.image = load_image('image/kirby/maxBullet.png')
        pass
    def update(self):
        self.x += 70
        self.frame= (self.frame+1)%6



        pass
    def render(self):
        self.image.clip_draw(self.frame*232,0,232,150,self.x,self.y)
        pass


    def getX(self): return self.x
    def getKind(self): return self.size
    def getDamage(self): return self.damage
    pass

class starBullet:
    image = None
    def __init__(self, point):
        self.x, self.y = point[0], point[1]
        self.damage = 5
        self.size = 1
        self.frame=0
        if starBullet.image == None:
            starBullet.image = load_image('image/kirby/StarBullet.png')
        pass
    def update(self):
        self.x += 50
        self.frame= (self.frame+1)%8
        pass
    def render(self):
        self.image.clip_draw(self.frame*30,0,30,30,self.x,self.y)
        pass


    def getX(self): return self.x
    def getKind(self): return self.size
    def getDamage(self): return self.damage
    pass

class kirbyBoom:
    def __init__(self,point):
        self.x, self.y = point[0],point[1]
        self.activated = False
        self.limit = 1.0
        self.frame = 0
        self.readyImage = load_image("image/kirby/BoomBullet.png")
        self.actImage = load_image("image/kirby/BoomShot.png")
        pass
    def update(self):
        self.frame = (self.frame + 1) % 2
        self.limit -=0.01
        if self.limit < 0.3:
            self.activated = True

        if self.activated == False:
            self.x+=4
        else:
            self.x+=2
        pass
    def render(self):
        if self.activated == False:
            self.readyImage.clip_draw(self.frame*46,0,46,46,self.x,self.y)
        else:
            self.actImage.clip_draw(self.frame*512,0,512,512,self.x,self.y)
        pass

    def getPoint(self): return (self.x,self.y)
    def boomActivate(self): self.activated = True
    def getLimitTime(self): return self.limit
    pass