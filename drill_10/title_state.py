import game_framework
import main_state
import title_state
from pico2d import *

name = "TitleState"
image = None
logo_time = 0

def enter():
    global image
    open_canvas()
    image = load_image('title.png')


def exit():
    global image
    del(image)
    close_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass







def update():
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01
    pass


def pause():
    pass


def resume():
    pass





enter()
while True:
    handle_events()
    update()
    draw()

exit()
