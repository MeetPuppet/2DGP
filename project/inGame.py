from pico2d import *
import game_framework
import enum

def WINSIZEX(): return 1024
def WINSIZEY(): return 768

name = 'inGame'

running = True
player = None
count = 0

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


    def __init__(self):
        self.x, self.y =-10,WINSIZEY()//2
        self.dirX, self.dirY = 0, 0
        self.frameX, self.frameY = 0, 0
        self.chargeCount = 0
        self.countOn = False
        self.isEvent = True
        self.HP = 5
        self.boom = 2
        self.state = kirbyStatus.IDLE
        self.IDLE = load_image('image/kirby/kirbyIDLE.png')
        self.CHARGE = load_image('image/kirby/chargeLevel.png')
        self.MAX = load_image('image/kirby/FullShot.png')
        #pass
    def update(self):
        # frame control
        if self.state == kirbyStatus.READY:
            self.frameX = (self.frameX +1)%4
        else:
            self.frameX = (self.frameX +1)%8
        # frame control

        # status move
        if self.state == kirbyStatus.IDLE:
            if self.chargeCount >= 10:
                self.state = kirbyStatus.READY
            else:
                self.state = kirbyStatus.IDLE
        elif self.state == kirbyStatus.READY:
            if self.chargeCount >= 10 and self.chargeCount < 30 and self.frameX == 3:
                self.frameY = 1
            elif self.chargeCount >= 35:
                self.frameY = 2
        elif self.state == kirbyStatus.SHOT:
            if self.frameX == 7:
                self.state = kirbyStatus.IDLE
        elif self.state == kirbyStatus.DEAD:
            #use Effect
            pass
        # status move

        print(self.chargeCount)

        # event, can't move
        if self.isEvent:
            if self.state == kirbyStatus.IDLE:
                self.x = self.x + 5
                if(self.x>100):
                    self.isEvent = False
                delay(0.05)
                return
                pass
            elif self.state == kirbyStatus.DEAD:
                pass
        # event, can't move

        # move Locate
        self.x = self.x + 10 * self.dirX
        self.y = self.y + 10 * self.dirY
        if self.countOn == True:
            self.chargeCount = self.chargeCount + 1
        delay(0.05)
        # move Locate

       # pass
    def render(self):
        if self.state == kirbyStatus.IDLE:
            self.IDLE.clip_draw(self.frameX*48,0,48,40,self.x,self.y)
        elif self.state == kirbyStatus.READY:
            self.CHARGE.clip_draw(self.frameX*64,self.frameY*64,64,64,self.x,self.y)
        elif self.state == kirbyStatus.SHOT:
            self.MAX.clip_draw(self.frameX*120,0,120,80,self.x,self.y)

        #pass

    def getHP(self): return self.HP
    def getBoom(self): return self.boom

    def getState(self): return self.state
    def setState(self, state): self.state = state

    def setFrameYZero(self): self.frameY=0
    def setDirectX(self, num): self.dirX += num
    def setDirectY(self, num): self.dirY += num
    def getCount(self): return self.chargeCount
    def isCharge(self, BOOL): self.countOn = BOOL
    def resetCount(self): self.chargeCount=0
    def useBoom(self, num): self.boom -= num
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


class kirbyStatus(enum.Enum):
    IDLE = 0
    READY = 1
    SHOT = 2
    DEAD = 3

def enter():
    global player
    player = Kirby()
    pass


def exit():
    global player
    del(player)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        # command Locate
            # key down
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()

            if event.key == SDLK_RIGHT:
                player.setDirectX(1)
            elif event.key == SDLK_LEFT:
                player.setDirectX(-1)
            if event.key == SDLK_UP:
                player.setDirectY(1)
            elif event.key == SDLK_DOWN:
                player.setDirectY(-1)

            if event.key == SDLK_z:
                player.isCharge(True)
                # nomalBullet
                if event.key == SDLK_x:
                    player.useBoom(1)
                    # useBoom

            # key down

            # key up
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                player.setDirectX(-1)
            elif event.key == SDLK_LEFT:
                player.setDirectX(1)
            if event.key == SDLK_UP:
                player.setDirectY(-1)
            elif event.key == SDLK_DOWN:
                player.setDirectY(1)

            if event.key == SDLK_z:
                if player.getState() == kirbyStatus.READY:
                    if player.getCount() >= 35:
                        # charge Shot
                        player.setState(kirbyStatus.SHOT)
                    else:
                        # nomalBullet
                        player.setState(kirbyStatus.IDLE)
                    player.setFrameYZero()
                player.resetCount()
                player.isCharge(False)
            # key up
        # command Locate
def update():
    global player
    player.update()


def draw():
    clear_canvas()
    player.render()
    update_canvas()
