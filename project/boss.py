from pico2d import *

class Batafire:
    IDLE = None
    def __init__(self):
        self.x, self.y = 1500,768//2
        self.maxHP, self.HP = 500, 500
        self.frame = 0
        self.state = 0
        self.guarding = 0
        self.wait = 120
        self.falling = 5
        #실행초에 어딘가 이미지를 로드해놓고 교체하는 방식이라면
        self.IDLE = load_image("image/boss/batafireIDLE.png")
        self.READY = load_image("image/boss/batafireReady.png")
        self.FIRE = load_image("image/boss/batafireFire.png")
        self.CHARGE = load_image("image/boss/batafireCharge.png")
        self.DEAD = load_image("image/boss/batafireDead.png")
        pass
    def update(self,targetXY):
        if self.guarding > 0 : self.guarding -= 1
        if self.HP <= 0: self.state = 4

        if self.state == 0:
            self.frame = (self.frame + 1) % 10

            if targetXY[0] < 550 and self.x > 879:
                self.x-=8
                pass
            elif targetXY[0] >= 550 and self.x<1000:
                self.x+=8

            if targetXY[1] > self.y - 20:
                self.y+=5
                pass
            elif targetXY[1] < self.y- 50:
                self.y-=5
                pass

            self.wait -= 1
            if self.wait < 0:
                self.frame = 0
                self.state = 1
            pass

        elif self.state == 1:
            self.frame = self.frame + 1
            if self.frame == 3:
                if targetXY[0] > 200:
                    self.state = 2
                    self.wait = 30
                else:
                    self.state = 3
                self.frame = 0
            pass

        elif self.state == 2:
            self.wait -= 1
            self.frame = (self.frame + 1) % 4
            if self.wait < 0:
                self.wait = 120
                self.frame = 0
                self.state = 0
                pass
            pass
        elif self.state == 3:
            self.frame = (self.frame + 1) % 4
            if self.x > -300 :
                self.x-=50
            else:
                self.wait = 120
                self.frame = 0
                self.x = 1300
                self.state = 0

            pass
        elif self.state == 4:
            if self.falling > 0 : self.frame = 0
            else : self.frame = 1

            self.y+=self.falling
            self.falling-=0.2

            if self.falling > -1 :
                delay(0.1)

            pass
        pass
    def render(self):
        if self.state == 0:
            self.IDLE.clip_draw(self.frame * 428, 0 , 428, 448, self.x, self.y)
            pass
        if self.state == 1:
            self.READY.clip_draw(self.frame * 428, 0 , 428, 448, self.x, self.y)
            pass
        if self.state == 2:
            self.FIRE.clip_draw(self.frame * 428, 0 , 428, 448, self.x, self.y)
            pass
        if self.state == 3:
            self.CHARGE.clip_draw(self.frame * 428, 0 , 428, 448, self.x, self.y)
            pass
        if self.state == 4:
            self.DEAD.clip_draw(self.frame * 428, 0 , 428, 448, self.x, self.y)
            pass
        pass
    pass

    def downHP(self,damage):
        if self.guarding < 0:
            self.HP -= damage
            self.guarding = 10
        pass

    def getPoint(self): return (self.x, self.y)
    def getState(self): return self.state
    def getHP(self): return self.HP
    def Kill(self): self.HP = 0
