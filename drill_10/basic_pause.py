from pico2d import *
import game_framework
import main_state

name = "BasicPause"
image = None
mode = 0

def enter():
    global image
    image = load_image('new_pause.png')
    pass


def exit():
    global image
    del(image)
    pass


def update():
    global mode
    if mode == 0:
        mode = 1
    else:
        mode = 0
    delay(0.05)
    pass


def draw():
    global image

    global mode
    delay(0.3)

    clear_canvas()
    if mode == 0:
        image.draw(800//2, 600//2)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.change_state(main_state)
    pass


def pause(): pass


def resume(): pass
