from pico2d import *

import game_framework
#import start_state
import inGame


def WINSIZEX(): return 1024
def WINSIZEY(): return 768

open_canvas(WINSIZEX(),WINSIZEY())

game_framework.run(inGame)

close_canvas()