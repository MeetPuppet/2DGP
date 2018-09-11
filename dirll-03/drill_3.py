from pico2d import *

open_canvas()

grass = load_image('grass.png')

character = load_image('character.png')


mode=[0,0]

getTime=0.0

x=50

y=50

while True :
    print(x,y)
    
    clear_canvas_now()
    grass.draw_now(400,30)
    if mode[0]==0:
        
        if mode[1]==0:
            x+=10
            if x>=750 and y<=300:
                mode[1]=1
                
        elif mode[1]==1:
            y+=10
            if x>=400 and y>=550:
                mode[1]=2
                
        elif mode[1]==2:
            x-=10
            if x<=50 and y>=300:
                mode[1]=3
                
        elif mode[1]==3:
            y-=10
            if x<=400 and y<=50:
                mode[0]=1
                mode[1]=0

                
    elif mode[0]==1:
        
        if mode[1]==0:
            if x<400:
                x+=10
            else:
                getTime+=0.2
                x+=(10-getTime)
                y+=getTime
                if getTime>=10:
                    mode[1]=1
                    getTime=0.0
                    
        elif mode[1]==1:
            getTime+=0.2
            x-=getTime
            y+=(10-getTime)
            if getTime>=10:
                mode[1]=2
                getTime=0.0
                
        elif mode[1]==2:
            getTime+=0.2
            x-=10-getTime
            y-=getTime
            if getTime>=10:
                mode[1]=3
                getTime=0.0

        elif mode[1]==3:
            getTime+=0.2
            x+=getTime
            y-=(10-getTime)
            if getTime>=10:
                y=50
                mode[0]=0
                mode[1]=0
                getTime=0.0
                
    character.draw_now(x,y)
    delay(0.01)

close_canvas()
