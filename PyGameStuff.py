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
screen = py.display.set_mode([boardWidth, boardWidth + width + margin])
screen.fill([255,255,255])




#create array of 0s
array = []
for i in range(9):
    toAppend = []
    for j in range(9):
        toAppend.append(0)
    array.append(toAppend)

array = []
for row in originalBoard:
    array.append(list(row))

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


#Create Solve Button
font = py.font.Font('freesansbold.ttf',20)
rect0 = py.draw.rect(screen, [0,0,0], py.Rect(margin, boardWidth, 2*width + margin, width))
rect0 = (rect0[0] + round(width*0.25), rect0[1] + round(width*0.25), rect0[2], rect0[3])

text0 = font.render("Solve", True, (255,255,255))

screen.blit(text0,rect0)

#Create reset button
rect1 = py.draw.rect(screen, [0,0,0], py.Rect(3*margin + width*2, boardWidth, 2*width + margin, width))
rect1 = (rect1[0] + round(width*0.25), rect1[1] + round(width*0.25), rect1[2], rect1[3])

text1 = font.render("Reset", True, (255,255,255))

screen.blit(text1,rect1)


#Change Font For Gameloop
font = py.font.Font('freesansbold.ttf',32)

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
            for i in range(10):
                gridy = i
                if y < start:
                    break
                start += (width + margin)
                
            
            #Changes the value of the gridpoint
            #Will be removed after testing
            if (gridy <= 8):
                #This is where the user input will be taken
                if (originalBoard[gridy][gridx] == 0):
                    if (array[gridy][gridx] == 0):
                        array[gridy][gridx] = 1
                    else:
                        array[gridy][gridx] = 0
            elif (gridy > 8):
                #Solve button Clicked
                if (gridx < 2):
                    array = []
                    for row in solvedBoard:
                        array.append(list(row))
                #Reset triggered        
                elif (gridx < 4):
                    array = []
                    for row in originalBoard:
                        array.append(list(row))
            
            #print("({},{})".format(gridx,gridy))
     
    #Checks the value of the grid and writes accordingly
    currentX = float(margin)
    currentY = float(margin)
    for i in range(0,9):
        for j in range(0,9):
            #Creates Square
            if (originalBoard[i][j] == 0):
                rect = py.draw.rect(screen, [0,0,0], py.Rect(currentX, currentY, width, width))
            else:
                rect = py.draw.rect(screen, [50,50,50], py.Rect(currentX, currentY, width, width))
            #Initilizes text to be written in the square
            text = font.render("{}".format(array[i][j]), True, (255,255,255))
            #print(rect)
            
            #Changes the coordinates of the rect, so that the text is centred
            rect = (rect[0] + width//3.5,rect[1] + width//6,rect[2],rect[3])
            
            #Condition to only display text if it is non zero.
            if (array[i][j] != 0):
                screen.blit(text,rect)
            
            currentX += width + margin
        currentY += width + margin
        currentX = float(margin)
    #This was just here for testing sizing
    # py.draw.circle(screen, (0, 0, 255), (250, 250), margin/2)
    
    # Update the display
    py.display.flip()

# Done! Time to quit.
py.quit()