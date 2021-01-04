'''
This is the file that will initiate the GUI for my Sudoku Game
This file calls upon the "Sudoku.py" file for solving.
'''
def ifActive(array):
    #Loops through array and returns:
    #True and the location if found
    #Else returns False and [0,0]
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == True:
                return [True,[i,j]]
    return [False,[0,0]]


from Sudoku import *
from random import randrange
#from Menu import orgBoard
# Import and initialize the pygame library
import pygame as py
import time

#global orgBoard
    #orgBoard will now be passed in when mainFunction is called
def mainFunction(orgBoard):    
    #py.init()
    
    
    #Dimensional Variables for each square
    width = 40
    margin = 2
    boardWidth = 380
    
    #Bools for use when determining when to change to the victory screen.
    solvedClicked = False
    isWin = False
    
    #Calls the Board Solver from Sudoku.py and solves the orgBoard also located there:
    solvedBoard = SudokuSolverStart(orgBoard)
    
    # Set up the drawing window
    screen = py.display.set_mode([boardWidth, boardWidth + width + margin])
    screen.fill([255,255,255])
    
    
    py.draw.rect(screen, [120,120,120], py.Rect(0, 0, boardWidth, boardWidth))
    
    dividerColor = [255,255,255]
    #Creat horizontal blue bars
    py.draw.rect(screen, dividerColor, py.Rect(0, 3*margin + 3*width, boardWidth, margin))
    py.draw.rect(screen, dividerColor, py.Rect(0, 6*margin + 6*width, boardWidth, margin))
    #Create vertical blue bars
    py.draw.rect(screen, dividerColor, py.Rect(3*margin + 3*width, 0, margin, boardWidth))
    py.draw.rect(screen, dividerColor, py.Rect(6*margin + 6*width, 0, margin, boardWidth))
    #screen.blit(screen,rect9)
    
    
    #Create array that keeps track of active boxes
    isActive = []
    for i in range(9):
        toAppend = []
        for j in range(9):
            toAppend.append(False)
        isActive.append(toAppend)
    
    #create array of 0s for check
    correctnessArray = []
    for i in range(9):
        toAppend = []
        for j in range(9):
            toAppend.append(0)
        correctnessArray.append(toAppend)
    
    array = []
    for row in orgBoard:
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
    
    #Create check button
    rect2 = py.draw.rect(screen, [0,0,0], py.Rect(5*margin + width*4, boardWidth, 2*width + margin, width))
    rect2 = (rect2[0] + round(width*0.25), rect2[1] + round(width*0.25), rect2[2], rect2[3])
    
    text2 = font.render("Check", True, (255,255,255))
    
    screen.blit(text2,rect2)
    
    #Create hint button
    rect3 = py.draw.rect(screen, [0,0,0], py.Rect(7*margin + width*6, boardWidth, 2*width + margin, width))
    rect3 = (rect3[0] + round(width*0.5), rect3[1] + round(width*0.25), rect3[2], rect3[3])
    
    text3 = font.render("Hint", True, (255,255,255))
    
    screen.blit(text3,rect3)
    
    screen.blit(text2,rect2)
    
    #Create hint button
    font = py.font.Font('freesansbold.ttf',32)
    rect4 = py.draw.rect(screen, [255,25,25], py.Rect(9*margin + width*8, boardWidth, width, width))
    rect4 = (rect4[0] + round(width*0.23), rect4[1] + round(width*0.12), rect4[2], rect4[3])
    
    text4 = font.render("X", True, (255,255,255))
    
    screen.blit(text4,rect4)
    
    #Change Font For Gameloop
    font = py.font.Font('freesansbold.ttf',32)
    
    #VariableFor Tracking Previous click
    prevClick = [0,0]
    
    #Gameloop begins
    
    startTime = time.time()
    running = True
    
    while running:
    
        #This loops through events.
        for event in py.event.get():
            #Closes app if an exit was prompted
            if event.type == py.QUIT:
                py.quit()
                running = False
            #Click detection
            elif event.type == py.MOUSEBUTTONDOWN:
                #Resets previous click
                isActive[prevClick[0]][prevClick[1]] = False
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
                    
                if (isWin == True) & (gridy == 4) & (2 < gridx < 6):
                    return timeTaken
                    #running = False
                
                if (gridy <= 8):
                    #This is where the user input will be taken
                    if (orgBoard[gridy][gridx] == 0):
                    #     if (array[gridy][gridx] == 0):
                    #         array[gridy][gridx] = 1
                    #     else:
                    #         array[gridy][gridx] = 0
                        #Registers current click
                        isActive[gridy][gridx] = True
                        #Stores click for next round
                        prevClick = [gridy,gridx]
                elif (gridy > 8):
                    #Solve button Clicked
                    if (gridx < 2):
                        solvedClicked = True
                        array = []
                        for row in solvedBoard:
                            array.append(list(row))
                        #Reset CorrectnessArray
                        correctnessArray = []
                        for i in range(9):
                            toAppend = []
                            for j in range(9):
                                toAppend.append(0)
                            correctnessArray.append(toAppend)
                        
        
                    #Reset triggered        
                    elif (gridx < 4):
                        solvedClicked = False
                        array = []
                        for row in orgBoard:
                            array.append(list(row))
                        #Reset CorrectnessArray
                        correctnessArray = []
                        for i in range(9):
                            toAppend = []
                            for j in range(9):
                                toAppend.append(0)
                            correctnessArray.append(toAppend)
                            
                    #Add code for check
                    elif (gridx < 6):
                        incorrectLocations = checkValid(array)
                        #Reset correctnessArray
                        correctnessArray = []
                        for i in range(9):
                            toAppend = []
                            for j in range(9):
                                toAppend.append(0)
                            correctnessArray.append(toAppend)
                        #There are not any incorrect spots
                        if len(incorrectLocations) == 0:
                            pass
                        #Incorrect cells exist.
                        else:
                            for pos in incorrectLocations:
                                x = pos[1]
                                y = pos[0]
                                correctnessArray[y][x] = 1
                    #Hint was prompted
                    elif (gridx < 8):
                        #Code for check added, as part of the hint
                        incorrectLocations = checkValid(array)
                        #Reset correctnessArray
                        correctnessArray = []
                        for i in range(9):
                            toAppend = []
                            for j in range(9):
                                toAppend.append(0)
                            correctnessArray.append(toAppend)
                        #There are not any incorrect spots
                        if len(incorrectLocations) == 0:
                            pass
                        #Incorrect cells exist.
                        else:
                            for pos in incorrectLocations:
                                x = pos[1]
                                y = pos[0]
                                correctnessArray[y][x] = 1
                        
                        possible = False
                        #New hint code starts
                        #Loop checks to see if there exists a cell that can be filled, to avoid a crash
                        for i in range(len(array)):
                            for j in range(len(array)):
                                if((array[i][j] == 0) | (correctnessArray[i][j] == 1)):
                                    possible = True
                        #After determining if a cell can be filled we run a loop that exits once a pseudorandom cell is found that is writable.
                        if possible:            
                            x = randrange(9)
                            y = randrange(9)
                            while((array[y][x] != 0) & (correctnessArray[y][x] != 1)):
                                x = randrange(9)
                                y = randrange(9)
                            array[y][x] = solvedBoard[y][x]
                    
                    #Bottom Right Exit is triggered        
                    elif (gridx < 9):
                        running = False
            #Following mouseclick checks for KEYDOWN
            elif (event.type == py.KEYDOWN):
                activity = ifActive(isActive)
                if activity[0] == True:
                    x = activity[1][1]
                    y = activity[1][0]
                    #print("True")
                    if event.key == py.K_KP_ENTER:
                            #print("Enter")
                            isActive[y][x] = False
                    elif (event.key == py.K_BACKSPACE) | (event.key == py.K_DELETE):
                        array[y][x] = 0
                    else:
                        try:
                            int(event.unicode)
                            if event.unicode in "1234567890":
                            #User typed something after clicking on a box.
                                array[y][x] = int(event.unicode)
                        except:
                            pass
                            #array[y][x] = int(event.unicode)
                    # if event.unicode in "123456789":
                    # #User typed something after clicking on a box.
                    #     array[y][x] = int(event.unicode)
                    
                    
         
        #Checks the value of the grid and writes accordingly
        currentX = float(margin)
        currentY = float(margin)
        for i in range(0,9):
            for j in range(0,9):
                #Creates Square
                if (orgBoard[i][j] == 0):
                    if (correctnessArray[i][j] == 1):
                        rect = py.draw.rect(screen, [255,0,0], py.Rect(currentX, currentY, width, width))
                    else:
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
        
        #Victory Display when the board is finished
        if ((array == solvedBoard) & (solvedClicked == False)) | (isWin == True):
            
            if (isWin == False):
                #print("Is False")
                timeTaken = time.time() - startTime
            #You have won
            isWin = True
            
            #Create Menu Button after win
            font = py.font.Font('freesansbold.ttf',20)
            rect0 = py.draw.rect(screen, [75,200,75], py.Rect(4*margin+3*width, 5*margin+4*width, 3*width + 2*margin, width))
            rect0 = (rect0[0] + round(width*0.85), rect0[1] + round(width*0.25), rect0[2], rect0[3])
            
            text0 = font.render("Menu", True, (255,255,255))
            
            screen.blit(text0,rect0)
            
            #fix font for condition exit
            font = py.font.Font('freesansbold.ttf',32)
            
            #Display victory text
            rect0 = py.draw.rect(screen, [255,255,255], py.Rect(3*margin+2*width, 3*margin+2*width, 5*width + 4*margin, width))
            rect0 = (rect0[0] + round(width*0.2), rect0[1] + round(width*0.15), rect0[2], rect0[3])
            text0 = font.render("You've Won!", True, (75,200,75))
            screen.blit(text0,rect0)
            
            
            
        # Update the display
        py.display.flip()
    
    # Done! Time to quit.
    #py.quit()
    
if __name__ == "__main__":
    py.init()
    orgBoard = []
    for row in originalBoard:
        orgBoard.append(list(row))
    mainFunction(orgBoard)
    py.quit()