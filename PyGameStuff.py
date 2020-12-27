# Simple pygame program

# Import and initialize the pygame library
import pygame as py
py.init()

# Set up the drawing window
screen = py.display.set_mode([500, 500])

class Square(py.sprite.Sprite):
    def __init__(self, squareNumber):
        self.location = squareNumber
        self.surf.set_colorkey((255, 255, 255), py.RLEACCEL)

square1 = Square(1)


running = True
while running:

    # Did the user click the window close button?
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False



    # Flip the display
    py.display.flip()

# Done! Time to quit.
py.quit()