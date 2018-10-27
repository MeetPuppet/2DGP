from pico2d import *
import game_world
import random
import math

class Coin:
    image = None
    def __init__(self, point = (2000,2000)):
        self.x, self.y = point[0],point[1]
        self.dirX, self.dirY = -12,9
        self.angle = random.randint(-6,6)
        self.frame=0
        self.liveTime=5.0
        if Coin.image == None:
            Coin.image = load_image("image/item/coin.png");
            pass
        pass
    def update(self):
        self.frame=(self.frame+1)%9
        self.x+=math.cos(self.angle) * self.dirX
        if(self.x>1024-10 or self.x<0+10):
            self.dirX = self.dirX*(-1)
        elif self.x > 1024 :
            self.x = 1024-10

        self.y+= -math.sin(self.angle)*self.dirY
        if(self.y>768-10 or self.y<0+10):
            self.dirY = self.dirY*(-1)

        self.liveTime-=0.01

        if self.liveTime < 0:
            game_world.remove_object2(self, 3)
        pass
    def render(self):
        if self.liveTime < 2 and self.frame%3==0:
            pass
        else:
            self.image.clip_draw(self.frame*32,0,32,32,self.x,self.y)
        pass
    pass

    def getPoint(self): return (self.x, self.y)
    def getLiveTime(self): return self.liveTime

class PowerUp:
    image = None

    def __init__(self, point= (2000,2000)):
        self.x, self.y = point[0], point[1]
        self.dirX, self.dirY = 12, 9
        self.angle = random.randint(-6,6)
        self.frame = 0
        self.liveTime = 5.0
        if PowerUp.image == None:
            PowerUp.image = load_image("image/item/PowerUp.png")
            pass
        pass

    def update(self):
        self.frame+=1%3
        self.x += math.cos(self.angle) * self.dirX
        if (self.x > 1024 - 10 or self.x < 0 + 10):
             self.dirX = self.dirX * (-1)
        elif self.x > 1024:
            self.x = 1024 - 10

        self.y += -math.sin(self.angle) * self.dirY
        if (self.y > 768 - 10 or self.y < 0 + 10):
            self.dirY = self.dirY * (-1)

        self.liveTime -= 0.01
        if self.liveTime < 0:
            game_world.remove_object2(self, 3)
        pass

    def render(self):
        if self.liveTime < 2 and self.frame % 3 == 0:
            pass
        else:
            self.image.draw(self.x, self.y)
        pass

    pass

    def getPoint(self): return (self.x, self.y)
    def getLiveTime(self): return self.liveTime

class BoomUp:
    image = None
    def __init__(self, point = (2000,2000)):
        self.x, self.y = point[0],point[1]
        self.dirX, self.dirY = -12,9
        self.angle = random.randint(-6,6)
        self.frame = 0
        self.liveTime=5.0
        if BoomUp.image == None:
            BoomUp.image = load_image("image/item/Boom.png");
            pass
        pass
    def update(self):

        self.frame=(self.frame+1)%3
        self.x+=math.cos(self.angle) * self.dirX
        if(self.x>1024-10 or self.x<0+10):
            self.dirX = self.dirX*(-1)
        elif self.x > 1024 :
            self.x = 1024-10

        self.y+= -math.sin(self.angle)*self.dirY
        if(self.y>768-10 or self.y<0+10):
            self.dirY = self.dirY*(-1)

        self.liveTime-=0.01
        pass
    def render(self):
        if self.liveTime < 2 and self.frame%3==0:
            pass
        else:
            self.image.draw(self.x,self.y)
        pass
    pass

    def getPoint(self): return (self.x, self.y)
    def getLiveTime(self): return self.liveTime
