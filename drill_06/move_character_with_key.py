from pico2d import *


def handle_events():
    global running
    global way
    global x
    global frameY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running=False
        elif event.type == SDL_KEYDOWN and frameY>1:
            if event.key == SDLK_RIGHT:
                way+=1
                frameY=1
            elif event.key == SDLK_LEFT:
                way-=1
                frameY=0
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP and frameY < 2:
            if event.key == SDLK_RIGHT:
                way-=1
                frameY=3
            elif event.key == SDLK_LEFT:
                way+=1
                frameY=2

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
frameY=3
way=0

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * frameY, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x+=way*10
    delay(0.02)

close_canvas()

