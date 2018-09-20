from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280,1024

def handle_events():
    global running
    global cursorX,cursorY
    global targetX,targetY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursorX, cursorY = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                targetX,targetY=cursorX,cursorY

def get_move(targetX, targetY):
    global x,y
    if(targetX<x):
        x-=1
    elif(targetX>x):
        x+=1


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x,y = KPU_WIDTH//2, KPU_HEIGHT//2
targetX, targetY = KPU_WIDTH//2, KPU_HEIGHT//2
cursorX, cursorY = 0,0
frameX=0
frameY=2
show_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH//2,KPU_HEIGHT//2)
    cursor.draw(cursorX+22,cursorY-22)
    character.clip_draw(frameX*100,frameY*100,100,100,x,y)
    update_canvas()
    frameX=(frameX+1)%8

    delay(0.01)

    handle_events()
    get_move(targetX,targetY)

close_canvas()