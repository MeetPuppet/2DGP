from pico2d import *
import game_framework
import enum
import random
import math

from Kirby import Kirby

from kirbyBullets import kirbyBullet1
from kirbyBullets import kirbyBullet2
from kirbyBullets import maxBullet
from kirbyBullets import starBullet
from kirbyBullets import kirbyBoom

from backGround import Stage

from Items import Coin
from Items import PowerUp
from Items import BoomUp

from boss import Batafire
from minions import Scarfy
from minions import SirKibble

#kirby state
IDLE, READY, SHOT, DEAD = range(4)

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

class enemyBullet:
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass
    pass


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
                bossList += [Batafire()]
            if event.key == SDLK_m:
                minion1List += [Scarfy(0)]
                minion1List += [Scarfy(1)]
                minion1List += [Scarfy(2)]
                minion1List += [Scarfy(3)]
            if event.key == SDLK_n:
                minion2List += [SirKibble()]
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
                if player.getState() == READY:
                    if player.getCount() >= 35:
                        # charge Shot
                        bulletList+=[maxBullet(player.getPoint())]
                        player.setState(SHOT)
                    else:
                        # nomalBullet
                        bulletList+=[kirbyBullet2(player.getPoint())]
                        player.setState(IDLE)
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
