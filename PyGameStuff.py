'''
This is the file that will initiate the GUI for my Sudoku Game
This file calls upon the "Sudoku.py" file for solving.
'''
from Sudoku import *
# Import and initialize the pygame library
import pygame as py
py.init()


#Dimensional Variables for each square
width = 40
margin = 2
boardWidth = 380


#Calls the Board Solver from Sudoku.py and solves the originalBoard also located there:
solvedBoard = SudokuSolverStart(originalBoard)

# Set up the drawing window
screen = py.display.set_mode([boardWidth, boardWidth])
screen.fill([255,255,255])


#The following loop creates the 9x9 grid on the board.
currentX = float(margin)
currentY = float(margin)
for i in range(0,9):
    for j in range(0,9):
        py.draw.rect(screen, [0,0,0], py.Rect(currentX, currentY, width, width))
        currentX += width + margin
    currentY += width + margin
    currentX = float(margin)
    





#Gameloop begins
running = True
while running:

    #This loops through events.
    for event in py.event.get():
        #Closes app if an exit was prompted
        if event.type == py.QUIT:
            running = False

    #This was just here for testing sizing
    # py.draw.circle(screen, (0, 0, 255), (250, 250), margin/2)
    
    # Update the display
    py.display.flip()

# Done! Time to quit.
py.quit()