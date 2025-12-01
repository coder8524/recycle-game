import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "recycle paper bag"

levels = 5
current_level = 1
trash_items = ["batteryimg","bottleimg","chipsimg","trash bag"]
actors = []
animations = []
game_done = False
gameover = False


def draw():
    screen.blit("world",(0,0))

    if gameover:
        screen.draw.text("game over",(400,300), fontsize = 80, color = "red")

    elif game_done:
        screen.draw.text("victory!!!",(400,300), fontsize = 80, color = "green")
    
    else:
       for actor in actors:
            actor.draw()
    
   
    
    
def game_compleet():
    global game_done
    if current_level >= 6:
        game_done = True



def update():
    pass

def create_actors():
    images = ["paperimg"]
    for i in range(current_level):
        item = random.choice(trash_items)
        images.append(item)

    for image in images:
        actor = Actor(image)
        actors.append(actor)

    number_of_gaps = current_level + 2
    gapsize = 800 // number_of_gaps
    random.shuffle(actors)

    for actor in actors:
        position = actors.index(actor) + 1 
        actor.pos = position * gapsize, 0
    
    for actor in actors:
        animation = animate(actor, y = HEIGHT,duration = 5, on_finished = game_over)
        animations.append(animation)

        
def game_over():
    global gameover
    gameover = True


def stop_animation():
    for animation in animations:
        if animation.running:
            animation.stop()
    

        
def on_mouse_down(pos):
    global current_level
    for actor in actors:
        if actor.collidepoint(pos):
            if actor.image == "paperimg":
                stop_animation()
                current_level += 1
                if current_level >= 6:
                    game_compleet()
                else:                    
                    actors.clear()
                    create_actors()
            else:
                game_over()






create_actors()

pgzrun.go()




    



