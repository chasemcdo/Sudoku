# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 01:38:22 2020
Attempt to create a game of Suduko
@author: chase
"""

toCheck = [1,2,3,4,5,6,7,8,9]

foundValues = []

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

'''
def backTrack(board,location):
    # Need to check previously changed values to get an acceptable value for this current position.
    y = location[0]
    x = location[1]
    
    for pos in range(0,len(board[y])): #Row
        if ((checked[y][pos] == 1) & (pos != x) & (board[y][pos] not in foundValues)):
            
            #print("test")
            #return check(board,[pos,y])
            break
            
    for pos in range(0,len(board)): #Column
        if ((checked[pos][x] == 1) & (pos != x)):
            #return check(board,[pos,x])
            break
'''    
    
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
        
        
    if (len(checked[y][x]) == 1):
        board[y][x] = checked[y][x][0]
        #print(checked[y][x][0])
        checked[y][x] = []
    #Need to add conditions for when none of the values fit.
    #So when we need to go and recheck previous values
    #backTrack(board,location)
    
    return board


def CheckLengths():
    length = 0
    for i in range(0,len(checked)):
            
            for j in range(0,len(checked[0])):
                if (len(checked[i][j]) > length):
                    length = len(checked[i][j])
                    
    return length

def SudokuSolverStart(gameBoard):
    boardCopy = []
    for i in range(0,len(gameBoard)):
        boardCopy.append(list(gameBoard[i])) #Copy the list. Has to be done as a loop otherwise they are not separate lists
    length = 10
    count = 0
    while(length > 1):
        for i in range(0,len(boardCopy)):
            
            for j in range(0,len(boardCopy[0])):
                if((boardCopy[i][j] == 0)):
                    #temp = 
                    boardCopy = check(boardCopy,[i,j])    #Loops through every digit checking if it needs to be replaced.
                    # if (temp != None):
                    #     boardCopy[i][j] = temp
        length = CheckLengths()
        # print(length)
        # for i in checked:
        #      print(i)
        count += 1
        #print(count)
        if (count > 10000):
            break
                
                #print(boardCopy[i][j])
    
    
    #print("{}\n\n{}\n".format(gameBoard,boardCopy))
    return boardCopy
    
if __name__ == "__main__":
    
    #check(gameBoard,[0,0])
    #print("{}\n".format(gameBoard))
    for i in originalBoard: #Prints out starting board, loop is used for readability
        print(i)
    print("\n")
    solvedBoard = SudokuSolverStart(originalBoard)
    
    #print("{}\n".format(solvedBoard))
    for i in solvedBoard: #Prints out "solved" board, loop is used for readability
        print(i)
    
    print("\n")
    
    for i in checked:
        print(i)
