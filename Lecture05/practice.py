from pico2d import *

def handle_event() :
    global running
    global dir
    global frameY

    for event in get_events():
        if event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dir+=1
                frameY=1
            elif event.key==SDLK_LEFT:
                dir-=1
                frameY=0
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                dir-=1
            elif event.key==SDLK_LEFT:
                dir+=1

open_canvas()
grass = load_image("grass.png")
character = load_image("animation_sheet.png")

running=True
x=800//2
frameX,frameY=0,0
dir=0

while True :
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frameX*100,frameY*100,100,100,x,90)
    update_canvas()

    handle_event()

    x+=dir*5
    frameX=(frameX+1)%8
    delay(0.02)

close_canvas()