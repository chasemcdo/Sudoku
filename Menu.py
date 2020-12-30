# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:05:39 2020

@author: chase
"""

from AppInterface import *
from random import randrange
from BoardBank import *
#Initialize PyGame
py.init()


global orgBoard
orgBoard = []
for i in range(9):
    toAppend = []
    for j in range(9):
        toAppend.append(0)
    orgBoard.append(toAppend)
    
    
#Calls the Board
#mainFunction()

#Dimensional Variables for each square
width = 40
margin = 2
boardWidth = 380

#Set font
font = py.font.Font('freesansbold.ttf',20)

playing = True
while playing:

    # Set up the drawing window
    screen = py.display.set_mode([boardWidth, boardWidth + width + margin])
    screen.fill([0,0,0])
    
    #Create Welcome Text
    rect0 = py.draw.rect(screen, [0,0,0], py.Rect(0, 2*margin + 1*width, 3*width + 2*margin, width))
    rect0 = (rect0[0] + round(width*1.3), rect0[1] + round(width*0.25), rect0[2], rect0[3])
    text0 = font.render("Welcome to my Sudoku Game", True, (255,255,255))
        
    screen.blit(text0,rect0)
    
    #Create Credit Text
    rect0 = py.draw.rect(screen, [0,0,0], py.Rect(0, 2*margin + 2*width, 3*width + 2*margin, width))
    rect0 = (rect0[0] + round(width*2.25), rect0[1] + round(width*0.25), rect0[2], rect0[3])
    text0 = font.render("By Chase McDougall", True, (255,255,255))
        
    screen.blit(text0,rect0)
    
    #Create Solve Button
    rect0 = py.draw.rect(screen, [50,50,50], py.Rect(4*margin + 3*width, 4*margin + 3*width, 3*width + 2*margin, width))
    rect0 = (rect0[0] + round(width*0.9), rect0[1] + round(width*0.25), rect0[2], rect0[3])
        
    text0 = font.render("Start", True, (255,255,255))
        
    screen.blit(text0,rect0)

    #Create Exit Button
    rect1 = py.draw.rect(screen, [50,50,50], py.Rect(4*margin + 3*width, 6*margin + 5*width, 3*width + 2*margin, width))
    rect1 = (rect1[0] + round(width*1.05), rect1[1] + round(width*0.25), rect1[2], rect1[3])
        
    text1 = font.render("Exit", True, (255,255,255))
        
    screen.blit(text1,rect1)

    # Did the user click the window close button?
    for event in py.event.get():
        if event.type == py.QUIT:
            playing = False

        elif event.type == py.MOUSEBUTTONDOWN:
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
            if (2 < gridx < 6):
            #Start button clicked:   
                if (gridy == 3):
                    boardNumber = randrange(len(board))
                    #global orgBoard
                    #print(board[boardNumber])
                    #print("\n")
                    orgBoard = []
                    for row in board[boardNumber]:
                        orgBoard.append(list(row))
                        
                    mainFunction(orgBoard)
            #Exit button clicked
                elif (gridy == 5):
                    playing = False
            
            #print("{},{}".format(gridx,gridy))
                
    # Flip the display
    py.display.flip()

# Done! Time to quit.
py.quit()