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
game_over = False


def draw():
    screen.blit("world",(0,0))

    for actor in actors:
        actor.draw()
        if game_over():
            screen.draw.text("game over", fontsize = 40, color = "red",(400,300))
    
    



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
        animation = animate(actor, y = HEIGHT,duration = 5)
        animations.append(animation)
        
def gameover():
    global game_over
    game_over = True
    

        
def on_mouse_down(pos):
    global current_level
    for actor in actors:
        if actor.collidepoint(pos):
            if actor.image == "paperimg":
                current_level += 1
                actors.clear()
                create_actors()
            else:
                gameover()






create_actors()

pgzrun.go()




    



