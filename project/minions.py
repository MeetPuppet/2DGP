from pico2d import *
import random


class Scarfy:
    image =None
    def __init__(self,moveNumber):
        self.pattern = moveNumber
        self.shotTime = 30
        self.isDead = 0
        self.isDown = 0
        self.jumpPower = 10
        self.gravity = 2.5
        self.frame = 0
        self.liveTime = 0
        if moveNumber%2 == 0:
            self.x, self.y = 1074, 610
            pass
        else:
            self.x, self.y = 1074, 300
            pass

        if Scarfy.image == None:
            Scarfy.image = load_image("image/minion/scarfy.png")
            pass
        pass
    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.shotTime > 0 : self.shotTime-=1
        if self. pattern == 0:
            self.x = (2*self.liveTime**2-3*self.liveTime+1)*1074 + (-4*self.liveTime**2+4*self.liveTime)*350 + (2*self.liveTime**2-self.liveTime)*1074
            self.y = (2*self.liveTime**2-3*self.liveTime+1)*768 + (-4*self.liveTime**2+4*self.liveTime)*600 + (2*self.liveTime**2-self.liveTime)*350
            self.liveTime+=0.015
            pass

        elif self.pattern == 1:
            self.x = (2*self.liveTime**2-3*self.liveTime+1)*1074 + (-4*self.liveTime**2+4*self.liveTime)*350 + (2*self.liveTime**2-self.liveTime)*1074
            self.y = (2*self.liveTime**2-3*self.liveTime+1)*0 + (-4*self.liveTime**2+4*self.liveTime)*168 + (2*self.liveTime**2-self.liveTime)*418
            self.liveTime+=0.015
            pass
        elif self. pattern >= 2:
            if self.shotTime < 0: self.shotTime = 30
            self.jumpPower -= self.gravity
            self.x -= 15
            if self.isDown == 0:
                self.y += self.jumpPower
            if self.jumpPower > 10:
                self.gravity*=-1
            elif self.jumpPower < -10:
                self.gravity*=-1

            pass
        pass
    def render(self):
        self.image.clip_draw(self.frame*50,0,50,50,self.x,self.y)
        pass
    def getPoint(self): return (self.x, self.y)
    def getState(self): return self.isDead
    def Kill(self): self.isDead = 1
    def getSize(self): return 0
    def shotTiming(self): return self.shotTime

    pass

class SirKibble:
    image =None
    def __init__(self):
        self.x, self.y = random.randint(512,900), -100
        self.jumpPower = random.randint(20,28)
        self.isDead = 0
        self.frame = 0
        if SirKibble.image == None:
            SirKibble.image = load_image("image/minion/SirKibble.png")
            pass
        pass
    def update(self):
        if self.jumpPower > 1:
            self.frame = 0
        elif self.jumpPower < 1:
            self.frame = 3
        else:
            if self.frame != 2:
                self.frame = (self.frame + 1) % 3
        self.y = self.y+self.jumpPower
        self.jumpPower-=0.5
        pass
    def render(self):
        self.image.clip_draw(self.frame*72,0,72,72,self.x,self.y)
        pass

    def getPoint(self): return (self.x, self.y)
    def getState(self): return self.isDead
    def Kill(self): self.isDead = 1
    def getFrame(self): return self.frame
    pass
