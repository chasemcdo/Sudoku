# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:47:54 2020


This file aims to create a random Sudoku board and then work backwards to create a board that can then be played from.
@author: Chase McDougall
"""
#import pseudo random number generator
from random import randrange
from Sudoku import findQuadrant
from Sudoku import getBounds

toCheck = [1,2,3,4,5,6,7,8,9]

#Array of checked values for every position
checked = [
          [[],[],[],[],[],[],[],[],[]],
          [[],[],[],[],[],[],[],[],[]],
          [[],[],[],[],[],[],[],[],[]],
          [[],[],[],[],[],[],[],[],[]],
          [[],[],[],[],[],[],[],[],[]],
          [[],[],[],[],[],[],[],[],[]],
          [[],[],[],[],[],[],[],[],[]],
          [[],[],[],[],[],[],[],[],[]],
          [[],[],[],[],[],[],[],[],[]]
          ]

def checkForZeros(board):
    '''
    This function will check for zeros in the array.
    If the array contains a zero it will return True.
    If has no more zeros it will return False
    '''
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (board[i][j] == 0):
                #Found zero return True
                return True
    #No zeros return False
    return False

def check(board,location): 
    #board is 9x9 matrix, location is 1x2 matrix of the location
    #returns the predicted value of this location.
    #foundValues = []
    y = location[0]
    x = location[1]
    #currVal = board[y][x]
    #print("{}\n".format(checked))
    #print(y,x,checked[y][x])
    #if((len(checked[y][x]) > 1) | (len(checked[y][x]) == 0)):
    checked[y][x] = list(toCheck)
    for i in range(0,len(board[0])): #Check row, and pop found values from the list of possible values
        if (board[y][i] in checked[y][x]):
            checked[y][x].pop(checked[y][x].index(board[y][i]))
               
    for i in range(0,len(board[0])): #Check column, and pop found values from the list of possible values
        if (board[i][x] in checked[y][x]):
            checked[y][x].pop(checked[y][x].index(board[i][x]))
        
    quadrant = findQuadrant(location) #Calls a function that will check which "quadrant" the point is, since there can only be one of each number in each "qudrant"
    bounds = getBounds(quadrant) #Calls a function that will give us the bounds for our loop
    
    #print("Test:\n{}\n{}\n".format(quadrant,bounds))
    for i in range(bounds[0][0], (bounds[0][1]+1)):
        for j in range(bounds[1][0], bounds[1][1]+1):
            if (board[i][j] in checked[y][x]):
                #print("Triggered?")
                checked[y][x].pop(checked[y][x].index(board[i][j]))
            
    # if (len(checked[y][x]) == 1):
    #     board[y][x] = checked[y][x][0]
    #     #print(checked[y][x][0])
    #     checked[y][x] = []
    #Need to add conditions for when none of the values fit.
    #So when we need to go and recheck previous values
    #backTrack(board,location)
    
    return board

def checkValidity(board):
    '''
    Checks if the board violates any rules.
    Returns True if it is a valid board.
    Returns False if it breaks a rule.
    '''
    for y in range(len(board)):
        for x in range(len(board[0])):
            currVal = board[y][x]
            if (currVal != 0):
                for i in range(0,len(board[0])): #Check row, and pop found values from the list of possible values
                    if (x != i):
                        if (board[y][i] == currVal):
                            return False
                   
                for i in range(0,len(board[0])): #Check column, and pop found values from the list of possible values
                    if (y != i):
                        if (board[i][x] == currVal):
                            return False
                quadrant = findQuadrant([y,x]) #Calls a function that will check which "quadrant" the point is, since there can only be one of each number in each "qudrant"
                bounds = getBounds(quadrant) #Calls a function that will give us the bounds for our loop
                
                for i in range(bounds[0][0], (bounds[0][1]+1)):
                    for j in range(bounds[1][0], bounds[1][1]+1):
                        if (i != y) & (j != x):
                            if (board[i][j] == currVal):
                                return False
    return True
   
def zeroCounter(board):
#Counts the number of zeros on a given board             
    count = 0
    
    for i in range(9):
        for j in range(9):
            if (board[i][j] == 0):
                count += 1
    return count            
    
def getCheckedLength(board):
    #Receives board and returns the length OF the longest possible list
    longLength = 0
    
    for i in range(9):
        for j in range(9):
            location = [i,j]
            check(board,location)
    
    for i in range(len(checked)):
        for j in range(len(checked[i])):
            if (len(checked[i][j]) > longLength) & (board[i][j] == 0):
                longLength = len(checked[i][j])
                
    return longLength

def filledBoardGenerator():
    count = 0
    thrown = 0
    #creates a blank 9x9 board
    board = []
    for i in range(9):
        toAppend = []
        for j in range(9):
            toAppend.append(0)
        board.append(list(toAppend))
        
    while (checkForZeros(board)):
        #Generate random numbers for use in generating the board
        x = randrange(9)
        y = randrange(9)
        num = randrange(1,10)
        
        if (board[y][x] != 0):
            count += 1
            continue
        
        #Create copy of the board to make sure that this addition doesn't violate any rules of Sudoku
        boardCopy = []
        for row in board:
            boardCopy.append(list(row))
        
        boardCopy[y][x] = num
        #Call function that tests if boardCopy is valid
        
        if (checkValidity(boardCopy) == True):
            count = 0
            board = []
            for row in boardCopy:
                board.append(list(row))
            
            # for row in board:
            #     print("{}".format(row))
        
        else:
            count += 1
          
        for row in board:
            print(row)
        print("{}\n".format(getCheckedLength(board)))    
        
        if (getCheckedLength(board) == 0) & (zeroCounter(board) == 0):
            break
        
        elif (getCheckedLength(board) == 0):
            break
        
        if (count >= 10000):
            count = 0
            thrown += 1
            
            for row in board:
                print("{}".format(row))
            print("{},\t{}\n".format(zeroCounter(board),thrown))
            
            board = []
            for i in range(9):
                toAppend = []
                for j in range(9):
                    toAppend.append(0)
                board.append(list(toAppend))
        
    return board

if __name__ == "__main__":
    board = filledBoardGenerator()
    
    for row in board:
        print(row)