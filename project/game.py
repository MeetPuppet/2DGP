from pico2d import *
import enum

def WINSIZEX(): return 1024
def WINSIZEY(): return 768

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class UI:#maybe unused
    class where(enum.Enum):
        OUTGAME = 0
        INGAME = 1
    class type(enum.Enum):
        OUTGAME = 0
        INGAME = 1
    def __init__(self, inGame, type):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass

class Kirby:
    class status(enum.Enum):
        IDLE = 0
        READY = 1
        SHOT = 2
        DEAD = 3

    def __init__(self):
        self.x, self.y =-10,WINSIZEY()//2
        self.dirX, self.dirY = 0, 0
        self.frameX, self.frameY = 0, 0
        self.chargeCount = 0
        self.countOn = 0
        self.isEvent = True
        self.HP = 5
        self.boom = 2
        self.state = self.status.IDLE
        self.IDLE = load_image('image/kirby/kirbyIDLE.png')
        self.CHARGE = load_image('image/kirby/chargeLevel.png')
        self.MAX = load_image('image/kirby/FullShot.png')
        #pass
    def update(self):
        # frame control
        if self.state == self.status.READY:
            self.frameX = (self.frameX +1)%4
        else:
            self.frameX = (self.frameX +1)%8
        # frame control

        # status move
        if self.state == self.status.IDLE:
            if self.chargeCount >= 10:
                self.state = self.status.READY
            else:
                self.state = self.status.IDLE
        elif self.state == self.status.READY:
            if self.chargeCount >= 10 and self.chargeCount < 30 and self.frameX == 3:
                self.frameY = 1
            elif self.chargeCount >= 50:
                self.frameY = 2
        elif self.state == self.status.SHOT:
            if self.frameX == 7:
                self.state = self.status.IDLE
        elif self.state == self.status.DEAD:
            #use Effect
            pass
        # status move

        #print(self.chargeCount)

        # event, can't move
        if self.isEvent:
            if self.state == self.status.IDLE:
                self.x = self.x + 5
                if(self.x>100):
                    self.isEvent = False
                delay(0.05)
                return
                pass
            elif self.state == self.status.DEAD:
                pass
        # event, can't move

        # command Locate
        events = get_events()
        for event in events:
            # key down
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dirX+=1
                elif event.key == SDLK_LEFT:
                    self.dirX-=1
                if event.key == SDLK_UP:
                    self.dirY+=1
                elif event.key == SDLK_DOWN:
                    self.dirY-=1

                if event.key == SDLK_z:
                    self.countOn += 1
                    # nomalBullet
                if event.key == SDLK_x:
                    self.boom -= 1
                    # useBoom

            # key down

            # key up
            if event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dirX-=1
                elif event.key == SDLK_LEFT:
                    self.dirX+=1
                if event.key == SDLK_UP:
                    self.dirY-=1
                elif event.key == SDLK_DOWN:
                    self.dirY+=1

                if event.key == SDLK_z:
                    self.countOn = 0
                    if self.state == self.status.READY:
                        if self.chargeCount >= 50:
                            # charge Shot
                            self.frameY = 0
                            self.state = self.status.SHOT
                        else:
                            self.state = self.status.IDLE
                            self.frameY = 0
                        self.countOn = 0
                        self.chargeCount = 0
            # key up
        # command Locate



        # move Locate
        self.x = self.x + 10 * self.dirX
        self.y = self.y + 10 * self.dirY
        self.chargeCount = self.chargeCount + 1*self.countOn
        delay(0.05)
        # move Locate

       # pass
    def render(self):
        if self.state == self.status.IDLE:
            self.IDLE.clip_draw(self.frameX*48,0,48,40,self.x,self.y)
        elif self.state == self.status.READY:
            self.CHARGE.clip_draw(self.frameX*64,self.frameY*64,64,64,self.x,self.y)
        elif self.state == self.status.SHOT:
            self.MAX.clip_draw(self.frameX*120,0,120,80,self.x,self.y)

        #pass

    def getState(self): return self.state
    pass

class Boss:
    class status(enum.Enum):
        IDLE = 0
        READY = 1
        FIRE = 2
        CHARGE = 3
        DEAD = 4
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass

class Minion:
    class status(enum.Enum):
        IDLE = 0
        ATTACK = 1
        DEAD = 2
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass

class Item:
    class status(enum.Enum):
        COIN = 0
        POWER = 1
        BOOM = 2
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass

class Stage:
    class status(enum.Enum):
        ONE = 0
        TWO = 1
        THREE = 2
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass

class effect:
    class status(enum.Enum):
        FORCE = 0
        SMOKE = 1
        COLLISION = 2
        DESTROY = 3
        BEAT = 4
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass



class kirbyBullet:
    class status(enum.Enum):
        NOMAL = 0
        HARD = 1
        MAX = 2
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass

class kirbyBoom:
    class status(enum.Enum):
        READY = 0
        BOOM = 1
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass


class enemyBullet:
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass

#field working place
class enemyManager:
    pass
class objectManager:#attack
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass
class mainGame:
    pass

running = True

open_canvas(WINSIZEX(), WINSIZEY())

count = 0
player = Kirby()

while running :
    player.update()
    clear_canvas()
    player.render()
    update_canvas()
