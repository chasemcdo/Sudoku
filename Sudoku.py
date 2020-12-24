# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 01:38:22 2020
Attempt to create a game of Suduko
@author: chase
"""

toCheck = [1,2,3,4,5,6,7,8,9]

originalBoard = [
          [9,1,0,3,4,0,0,0,7],
          [0,8,3,0,9,7,0,5,0],
          [4,2,7,0,0,0,0,1,0],
          [0,0,2,6,8,0,4,0,0],
          [7,0,4,2,0,9,0,0,0],
          [0,0,8,0,3,4,1,6,0],
          [8,0,0,0,0,0,0,4,0],
          [0,0,9,0,0,0,7,2,6],
          [0,5,6,0,0,3,8,0,1]
          ]

checked = [
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]
          ]

def check(board,location): 
    #board is 9x9 matrix, location is 1x2 matrix of the location
    #returns the predicted value of this location.
    y = location[0]
    x = location[1]
    currVal = board[y][x]
    checked[y][x] = 1
    for i in range(currVal,len(toCheck)): #loops through possible values
        found = 0
        for pos in range(0,len(board[y])):  #loops through row
            if(board[y][pos] == toCheck[i]):    #Checks point value to the current possible value
                found = 1                           #If they are equal break loop since this value doesn't work
                break
        if(found == 1):
            continue
        for pos in range(0,len(board)):
            if(board[pos][x] == toCheck[i]):    #Checks point value to the current possible value
                found = 1                           #If they are equal break loop since this value doesn't work
                break
            
        if(found == 0):
            return toCheck[i]
    #Need to add conditions for when none of the values fit.
    #So when we need to go and recheck previous values
    

def SudukoSolverStart(gameBoard):
    boardCopy = []
    for i in range(0,len(gameBoard)):
        boardCopy.append(list(gameBoard[i])) #Copy the list. Has to be done as a loop otherwise they are not separate lists
    
    for i in range(0,len(boardCopy)):
        
        for j in range(0,len(boardCopy[0])):
            if((boardCopy[i][j] == gameBoard[i][j]) & (boardCopy[i][j] == 0)):
                boardCopy[i][j] = check(boardCopy,[i,j])    #Loops through every digit checking if it needs to be replaced.
                
            
            
            #print(boardCopy[i][j])
    
    
    #print("{}\n\n{}\n".format(gameBoard,boardCopy))
    return boardCopy
    
if __name__ == "__main__":
    
    #check(gameBoard,[0,0])
    #print("{}\n".format(gameBoard))
    for i in originalBoard:
        print(i)
    print("\n")
    solvedBoard = SudukoSolverStart(originalBoard)
    
    #print("{}\n".format(solvedBoard))
    for i in solvedBoard:
        print(i)
