from pico2d import *

def WINSIZEX(): return 1024
def WINSIZEY(): return 768

IDLE, READY, SHOT, DEAD = range(4)

RIGHT_KEY_DOWN, RIGHT_KEY_UP, LEFT_KEY_DOWN,  LEFT_KEY_UP,\
UP_KEY_DOWN, UP_KEY_UP, DOWN_KEY_DOWN, DOWN_KEY_UP,\
Z_KEY_DOWN, Z_KEY_UP, X_KEY_DOWN= range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UP_KEY_DOWN,
    (SDL_KEYUP, SDLK_UP)  : UP_KEY_UP,

    (SDL_KEYDOWN, SDLK_DOWN): DOWN_KEY_DOWN,
    (SDL_KEYUP, SDLK_DOWN)  : DOWN_KEY_UP,

    (SDL_KEYDOWN, SDLK_LEFT): LEFT_KEY_DOWN,
    (SDL_KEYUP, SDLK_LEFT)  : LEFT_KEY_UP,

    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_KEY_DOWN,
    (SDL_KEYUP, SDLK_RIGHT)  : RIGHT_KEY_UP,

    (SDL_KEYDOWN, SDLK_z): Z_KEY_DOWN,
    (SDL_KEYUP, SDLK_z): Z_KEY_UP,

    (SDL_KEYDOWN, SDLK_x): X_KEY_DOWN,
}

next_state_table = {
    #필요 불분명함
    #적용형식 불분명
    #모든 상태변화는 내부의 chargeCount의 영향에서 옴
}

class Kirby:
    def __init__(self):
        self.x, self.y =-10,WINSIZEY()//2
        self.dirX, self.dirY = 0, 0
        self.frameX, self.frameY = 0, 0
        self.chargeCount = 0
        self.countOn = False
        self.isEvent = True
        self.maxHP = 5
        self.HP = 5
        self.boom = 2
        self.state = IDLE
        self.IDLE = load_image('image/kirby/kirbyIDLE.png')
        self.CHARGE = load_image('image/kirby/chargeLevel.png')
        self.MAX = load_image('image/kirby/FullShot.png')
        #pass

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]

            if key_event == UP_KEY_DOWN:
                self.dirY += 1
            elif key_event == UP_KEY_UP:
                self.dirY -= 1
            elif key_event == DOWN_KEY_DOWN:
                self.dirY -= 1
            elif key_event == DOWN_KEY_UP:
                self.dirY += 1

            if key_event == RIGHT_KEY_DOWN:
                self.dirX += 1
            elif key_event == LEFT_KEY_DOWN:
                self.dirX -= 1
            elif key_event == RIGHT_KEY_UP:
                self.dirX -= 1
            elif key_event == LEFT_KEY_UP:
                self.dirX += 1

            if key_event == Z_KEY_DOWN:
                self.dirX += 1
            elif key_event == Z_KEY_UP:
                self.dirX -= 1

            if key_event == X_KEY_DOWN:
                self.dirX += 1

        pass

    def update(self):
        # frame control
        if self.state == READY:
            self.frameX = (self.frameX +1)%4
        else:
            self.frameX = (self.frameX +1)%8
        # frame control

        # status move
        if self.state == IDLE:
            if self.chargeCount >= 10:
                self.state = READY
            else:
                self.state = IDLE
        elif self.state == READY:
            if self.chargeCount >= 10 and self.chargeCount < 30 and self.frameX == 3:
                self.frameY = 1
            elif self.chargeCount >= 35:
                self.frameY = 2
        elif self.state == SHOT:
            if self.frameX == 7:
                self.state = IDLE
        elif self.state == DEAD:
            #use Effect
            pass
        # status move

        #print(self.chargeCount)

        # event, can't move
        if self.isEvent:
            if self.state == IDLE:
                self.x = self.x + 5
                if(self.x>100):
                    self.isEvent = False
                return
                pass
            elif self.state == DEAD:
                pass
        # event, can't move

        # move Locate
        self.x = self.x + 10 * self.dirX
        if self.x>1024-24 or self.x<0 + 24:
            self.x = self.x - 15 * self.dirX
        self.y = self.y + 10 * self.dirY
        if self.y > 768 - 24 or self.y < 0 + 24:
            self.y = self.y - 15 * self.dirY
        if self.countOn == True:
            self.chargeCount = self.chargeCount + 1
        if self.HP > self.maxHP:
            self.HP = self.maxHP
        # move Locate



    def render(self):
        if self.state == IDLE:
            self.IDLE.clip_draw(self.frameX*48,0,48,40,self.x,self.y)
        elif self.state == READY:
            self.CHARGE.clip_draw(self.frameX*64,self.frameY*64,64,64,self.x,self.y)
        elif self.state == SHOT:
            self.MAX.clip_draw(self.frameX*120,0,120,80,self.x,self.y)
        #pass

    def getPoint(self): return (self.x,self.y)

    def getHP(self): return self.HP
    def heal(self): self.HP += 1
    def hit(self): self.HP -= 1

    def getBoom(self): return self.boom
    def setBoom(self,count): self.boom += count

    def getState(self): return self.state
    def setState(self, state): self.state = state

    def setFrameYZero(self): self.frameY=0
    def setDirectX(self, num): self.dirX += num
    def setDirectY(self, num): self.dirY += num

    def getCount(self): return self.chargeCount
    def isCharge(self, BOOL): self.countOn = BOOL
    def resetCount(self): self.chargeCount=0


    pass