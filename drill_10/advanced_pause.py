from pico2d import *
import game_framework
import basic_pause

name = "BasicPause"
image = None

def enter():
    global image
    image = load_image('new_pause.png')
    pass


def exit():
    global image
    del(image)
    pass


def update():
    pass


def draw():
    global image


    clear_canvas()
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
                game_framework.pop_state()
    pass


def pause(): pass


def resume(): pass
