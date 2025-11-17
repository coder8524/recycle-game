import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "recycle paper bag"

levels = 5
current_level = 1
trash_items = ["batteryimg","bottleimg","chipsimg","trash bag"]
actors = []

def draw():
    screen.blit("world",(0,0))

    for actor in actors:
        actor.draw()



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


    
        






create_actors()

pgzrun.go()




    



