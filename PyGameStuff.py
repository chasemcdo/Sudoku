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
screen = py.display.set_mode([boardWidth, boardWidth + round(width/2) + margin])
screen.fill([255,255,255])

#create array of 0s
array = []
for i in range(9):
    toAppend = []
    for j in range(9):
        toAppend.append(0)
    array.append(toAppend)



#The following loop creates the 9x9 grid on the board.
# currentX = float(margin)
# currentY = float(margin)
# for i in range(0,9):
#     for j in range(0,9):
#         py.draw.rect(screen, [0,0,0], py.Rect(currentX, currentY, width, width))
        
#         #print(array[i][j])
#         if array[i][j] == 1:
#             py.draw.rect(screen, [100,0,100], py.Rect(currentX, currentY, width, width))
        
#         currentX += width + margin
#     currentY += width + margin
#     currentX = float(margin)





#Gameloop begins
running = True
while running:

    #This loops through events.
    for event in py.event.get():
        #Closes app if an exit was prompted
        if event.type == py.QUIT:
            running = False
            
        #Click detection
        elif event.type == py.MOUSEBUTTONDOWN:
            #Gets the mouse position
            pos = py.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            #Finds the column
            start = (width + margin)
            for i in range(9):
                gridx = i
                if x < start:
                    break
                start += (width + margin)
            #Finds the row
            start = (width + margin)
            for i in range(9):
                gridy = i
                if y < start:
                    break
                start += (width + margin)
                
            #Changes the value of the gridpoint
            if (array[gridy][gridx] == 0):
                array[gridy][gridx] = 1
            else:
                array[gridy][gridx] = 0
                
                
            
                
            
            
            
            print("({},{})".format(gridx,gridy))
     
    #Checks the value of the grid and writes accordingly
    currentX = float(margin)
    currentY = float(margin)
    for i in range(0,9):
        for j in range(0,9):
            py.draw.rect(screen, [0,0,0], py.Rect(currentX, currentY, width, width))
        
            #print(array[i][j])
            if array[i][j] == 1:
                py.draw.rect(screen, [100,0,100], py.Rect(currentX, currentY, width, width))
            
            currentX += width + margin
        currentY += width + margin
        currentX = float(margin)
    #This was just here for testing sizing
    # py.draw.circle(screen, (0, 0, 255), (250, 250), margin/2)
    
    # Update the display
    py.display.flip()

# Done! Time to quit.
py.quit()