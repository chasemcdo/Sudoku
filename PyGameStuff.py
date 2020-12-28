# Simple pygame program

# Import and initialize the pygame library
import pygame as py
py.init()


#Dimensional Variables for each square
width = 40
margin = 2
boardWidth = 380

# Set up the drawing window
screen = py.display.set_mode([boardWidth, boardWidth])
screen.fill([255,255,255])

currentX = float(margin)
currentY = float(margin)
for i in range(0,9):
    for j in range(0,9):
        py.draw.rect(screen, [0,0,0], py.Rect(currentX, currentY, width, width))
        currentX += width + margin
    currentY += width + margin
    currentX = float(margin)
# class Square(py.sprite.Sprite):
#     def __init__(self, squareNumber):
#         self.location = squareNumber
#         self.surf.set_colorkey((255, 255, 255), py.RLEACCEL)


# square1 = Square(1)


running = True
while running:

    # Did the user click the window close button?
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False


    # py.draw.circle(screen, (0, 0, 255), (250, 250), margin/2)
    
    # Flip the display
    py.display.flip()

# Done! Time to quit.
py.quit()