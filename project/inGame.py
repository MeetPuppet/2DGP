from pico2d import *
import game_framework
import enum
import random
import math

def WINSIZEX(): return 1024
def WINSIZEY(): return 768

name = 'inGame'

running = True
player = None
stage = None
bulletList = []

coinList = []
powerUpList = []
boomUpList = []

boomList = []

minion1List = []
minion2List = []

bossList = []
count = 0


class UI:#maybe unused

    def __init__(self, inGame, type):

        pass
    def update(self):
        pass
    def render(self):
        self.a=0
    pass

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

        #print(self.chargeCount)

        # event, can't move
        if self.isEvent:
            if self.state == kirbyStatus.IDLE:
                self.x = self.x + 5
                if(self.x>100):
                    self.isEvent = False
                return
                pass
            elif self.state == kirbyStatus.DEAD:
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
        if self.state == kirbyStatus.IDLE:
            self.IDLE.clip_draw(self.frameX*48,0,48,40,self.x,self.y)
        elif self.state == kirbyStatus.READY:
            self.CHARGE.clip_draw(self.frameX*64,self.frameY*64,64,64,self.x,self.y)
        elif self.state == kirbyStatus.SHOT:
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

class kirbyBullet1:
    image = None
    def __init__(self, point):
        self.x, self.y = point[0], point[1]
        self.size = power
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
        self.size = 1;
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
        self.frame=random.randint(0,8)
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
    class status(enum.Enum):
        READY = 0
        BOOM = 1
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


class Boss:
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

class Minion1:
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

        if Minion1.image == None:
            Minion1.image = load_image("image/minion/scarfy.png")
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

class Minion2:
    image =None
    class status(enum.Enum):
        IDLE = 0
        ATTACK = 1
        DEAD = 2
    def __init__(self):
        self.x, self.y = random.randint(512,900), -100
        self.jumpPower = random.randint(20,28)
        self.isDead = 0
        self.frame = 0
        if Minion2.image == None:
            Minion2.image = load_image("image/minion/cirkyble.png")
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

class Coin:
    image = None
    def __init__(self, point):
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

        self.y+=math.sin(self.angle)*self.dirY
        if(self.y>768-10 or self.y<0+10):
            self.dirY = self.dirY*(-1)

        self.liveTime-=0.01
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

    def __init__(self, point):
        self.x, self.y = point[0], point[1]
        self.dirX, self.dirY = -12, 9
        self.angle = random.randint(-6, 6)
        self.frame = 0
        self.liveTime = 5.0
        if PowerUp.image == None:
            PowerUp.image = load_image("image/item/PowerUp.png");
            pass
        pass

    def update(self):
        self.frame+=1%3
        self.x += math.cos(self.angle) * self.dirX
        if (self.x > 1024 - 10 or self.x < 0 + 10):
             self.dirX = self.dirX * (-1)
        elif self.x > 1024:
            self.x = 1024 - 10

        self.y += math.sin(self.angle) * self.dirY
        if (self.y > 768 - 10 or self.y < 0 + 10):
            self.dirY = self.dirY * (-1)

        self.liveTime -= 0.01
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
    def __init__(self, point):
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

        self.y+=math.sin(self.angle)*self.dirY
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

class Stage:
    class status(enum.Enum):
        ONE = 0
        TWO = 1
        THREE = 2
    def __init__(self, stage):
        if(stage==0):
            self.frame1X, self.frame1Y =0,0
            self.frame2X, self.frame2Y =1024,0
        elif (stage == 1):
            self.frame1X, self.frame1Y =0,1
            self.frame2X, self.frame2Y =1024,1
        else:
            self.frame1X, self.frame1Y =0,2
            self.frame2X, self.frame2Y =1024,2
        self.image1 = load_image("image/map.jpg")
        self.image2 = load_image("image/map.jpg")
        pass
    def update(self):
        self.frame1X -= 20
        self.frame2X -= 20
        if self.frame1X < -1004:
            self.frame1X=self.frame1X*-1
        if self.frame2X < -1004:
            self.frame2X=self.frame2X*-1

        pass
    def render(self):
        self.image1.clip_draw(0,self.frame1Y*768,1024,768,self.frame1X+(1024//2),768//2)
        self.image2.clip_draw(0,self.frame2Y*768,1024,768,self.frame2X+(1024//2),768//2)
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
    global stage
    player = Kirby()
    stage = Stage(0)
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
    global bossList
    global bulletList
    global coinList
    global powerUpList
    global boomUpList
    global boomList
    global minion1List
    global minion2List
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        # command Locate
            # key down
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            if event.key == SDLK_0:
                coinList += [Coin((400,300))]
            if event.key == SDLK_1:
                powerUpList += [PowerUp((400,300))]
            if event.key == SDLK_2:
                boomUpList += [BoomUp((400,300))]

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
                bulletList+=[kirbyBullet1(player.getPoint())]
            if event.key == SDLK_x:
                player.setBoom(-1)
                boomList+=[kirbyBoom(player.getPoint())]
                # useBoom

            if event.key == SDLK_b:
                bossList += [Boss()]
            if event.key == SDLK_m:
                minion1List += [Minion1(0)]
                minion1List += [Minion1(1)]
                minion1List += [Minion1(2)]
                minion1List += [Minion1(3)]
            if event.key == SDLK_n:
                minion2List += [Minion2()]
            if event.key == SDLK_v:
                for boss in bossList:
                    boss.Kill()

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
                        bulletList+=[maxBullet(player.getPoint())]
                        player.setState(kirbyStatus.SHOT)
                    else:
                        # nomalBullet
                        bulletList+=[kirbyBullet2(player.getPoint())]
                        player.setState(kirbyStatus.IDLE)
                    player.setFrameYZero()
                player.resetCount()
                player.isCharge(False)
            # key up
        # command Locate
def update():
    delay(0.0395)
    stage.update()
    player.update()
    for bullet in bulletList:
        bullet.update()
        if bullet.getX() > 1024+130:
            bulletList.remove(bullet)
    #print(len(bulletList))
    for coin in coinList:
        coin.update()
        if coin.getLiveTime() < 0:
            coinList.remove(coin)
    for powerUp in powerUpList:
        powerUp.update()
        if powerUp.getLiveTime() < 0:
            powerUpList.remove(powerUp)
    for boomUp in boomUpList:
        boomUp.update()
        if boomUp.getLiveTime() < 0:
            boomUpList.remove(boomUp)
    for boom in boomList:
        boom.update()
        if boom.getLimitTime() < 0:
            boomList.remove(boom)
    #print(len(bossList))
    for boss in bossList:
        boss.update(player.getPoint())
        #print(boss.getState())
        #print(boss.getHP())
        if boss.getPoint()[1] <= -200 and boss.getHP() <= 0:
            bossList.remove(boss)
    #print(len(itemList))
    for minion1 in minion1List:
        minion1.update()
        if minion1.getPoint()[0] > 1080:
            minion1List.remove(minion1)
        elif minion1.getState() == 1:
            #위치값을 받아와서 effact 실행
            minion1List.remove(minion1)
            pass#
        if minion1.shotTiming() < 0:
            pass#적 총알 생성
    for minion2 in minion2List:
        minion2.update()
        if minion2.getPoint()[1] < -100:
            minion2List.remove(minion2)


def draw():
    clear_canvas()
    stage.render()
    player.render()
    for boss in bossList:
        boss.render()
    for bullet in bulletList:
        bullet.render()
    for coin in coinList:
        coin.render()
    for powerUp in powerUpList:
        powerUp.render()
    for boomUp in boomUpList:
        boomUp.render()
    for boom in boomList:
        boom.render()
    for minion1 in minion1List:
        minion1.render()
    for minion2 in minion2List:
        minion2.render()
    update_canvas()
