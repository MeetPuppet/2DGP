from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280,1024

def handle_events():
    global running
    global cursorX,cursorY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursorX, cursorY = event.x+22, KPU_HEIGHT - 1 - event.y-22
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def get_move():
    pass

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
    cursor.draw(cursorX,cursorY)
    character.clip_draw(frameX*100,frameY*100,100,100,x,y)
    update_canvas()
    frameX=(frameX+1)%8

    delay(0.02)

    handle_events()

close_canvas()