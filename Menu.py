# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 11:05:39 2020

@author: chase
"""

from AppInterface import *

#Initialize PyGame
py.init()

#Calls the Board
#mainFunction()

#Dimensional Variables for each square
width = 40
margin = 2
boardWidth = 380

# Set up the drawing window
screen = py.display.set_mode([boardWidth, boardWidth + width + margin])
screen.fill([255,255,255])

playing = True
while playing:

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
            print("{},{}".format(gridx,gridy))
                
    # Flip the display
    py.display.flip()

# Done! Time to quit.
py.quit()