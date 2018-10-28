from pico2d import *
import game_world
import random
class Batafire:
    IDLE = None
    READY = None
    FIRE = None
    CHARGE = None
    DEAD = None
    def __init__(self):
        self.x, self.y = 1500,768//2
        self.maxHP, self.HP = 500, 500
        self.radius = 150
        self.frame = 0
        self.state = 0
        self.guarding = 0
        self.wait = 180
        self.backMove = False
        self.UpMove = False
        self.falling = 5
        #실행초에 어딘가 이미지를 로드해놓고 교체하는 방식이라면
        if Batafire.IDLE == None:
            Batafire.IDLE = load_image("image/boss/batafireIDLE.png")
        if Batafire.READY == None:
            Batafire.READY = load_image("image/boss/batafireReady.png")
        if Batafire.FIRE == None:
            Batafire.FIRE = load_image("image/boss/batafireFire.png")
        if Batafire.CHARGE == None:
            Batafire.CHARGE = load_image("image/boss/batafireCharge.png")
        if Batafire.DEAD == None:
            Batafire.DEAD = load_image("image/boss/batafireDead.png")

        pass
    def update(self):
        if self.guarding > 0 : self.guarding -= 1
        if self.HP <= 0: self.state = 4

        if self.state == 0:
            self.frame = (self.frame + 1) % 10

            if self.backMove == True:
                self.x+=8
            else:
                self.x-=8
            if self.x > 974:
                if self.UpMove == True:
                    self.y+=5
                else:
                    self.y-=5

            if self.x < 612:
                self.backMove = True
                pass
            elif self.x > 974:
                self.backMove = False
                pass
            if self.y > 718:
                self.UpMove = False
                pass
            elif self.y < 100:
                self.UpMove = True
                pass


            self.wait -= 1
            if self.wait < 0:
                self.frame = 0
                self.state = 1
            pass

        elif self.state == 1:
            self.frame = self.frame + 1
            if self.frame == 3:
                if random.randint(0,1) == 0:
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
                self.wait = 180
                self.frame = 0
                self.state = 0
                pass
            pass
        elif self.state == 3:
            self.frame = (self.frame + 1) % 4
            if self.x > -300 :
                self.x-=50
            else:
                self.wait = 180
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

            if self.y < -150:
                game_world.remove_object2(self, 2)

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
    def getRadius(self): return self.radius
    def getState(self): return self.state
    def getHP(self): return self.HP
    def Kill(self): self.HP = 0
