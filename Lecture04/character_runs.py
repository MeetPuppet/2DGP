from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x=0
mode = 0

frameX=0
frameY=1
while(True):
    if(mode==0):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frameX*100,frameY*100,100,100,x,90)
        update_canvas()
        frameX=(frameX+1)%8
        x+=10
        delay(0.05)
        if(x>800):
            mode=1
            frameY=0
    elif(mode==1):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frameX*100,frameY*100,100,100,x,90)
        update_canvas()
        frameX=(frameX+1)%8
        x-=10
        delay(0.05)
        if(x<0):
            mode=0
            frameY=1


close_canvas()

