from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x,y
    global cursorX, cursorY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursorX, cursorY = event.x+22, KPU_HEIGHT-1-event.y-22
        if event.key == SDL_MOUSEBUTTONDOWN:
            targetX,targetY=cursorX,cursorY

        elif event.type == SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image("hand_arrow.png")

running = True
cursorX, cursorY=0,0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
targetX, targetY = x,y
frame = 0
show_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    cursor.draw(cursorX,cursorY)
    update_canvas()
    frame = (frame + 1) % 8

    if(targetX<x):
        x-=1
    elif targetX>x:
        x+=1

    if(targetY<y):
        y-=1
    elif targetY>y:
        y+=1

    print(targetX,targetY)

    delay(0.02)
    handle_events()

close_canvas()




