# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 01:38:22 2020
Attempt to create a game of Suduko
@author: chase
"""

toCheck = [1,2,3,4,5,6,7,8,9]

foundValues = []

originalBoard = [
          # [9,1,0,3,4,0,0,0,7],
          # [0,8,3,0,9,7,0,5,0],
          # [4,2,7,0,0,0,0,1,0],
          # [0,0,2,6,8,0,4,0,0],
          # [7,0,4,2,0,9,0,0,0],
          # [0,0,8,0,3,4,1,6,0],
          # [8,0,0,0,0,0,0,4,0],
          # [0,0,9,0,0,0,7,2,6],
          # [0,5,6,0,0,3,8,0,1]
          [7,0,1,9,0,0,0,8,0],
          [0,0,3,0,0,0,4,0,6],
          [0,0,6,0,0,8,0,0,0],
          [0,0,0,0,8,6,0,0,4],
          [0,0,0,7,1,5,0,0,0],
          [5,0,0,4,2,0,0,0,0],
          [0,0,0,5,0,0,6,0,0],
          [3,0,8,0,0,0,5,0,0],
          [0,2,0,0,0,4,3,0,1]
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
  
def findQuadrant(location):
    '''
    This function takes the coordinates and based on finds which of the 3x3 subsections the point is in.
    This is important because in Sudoku there can only be one of each number in these sections,
    so for example if 8/9 spots in the top left square, then we know what the 9th one in that section is.
    '''
    y = location[0]
    x = location[1]
    
    if(x <= 2): #These conditions get the x value
        quadrantx = 1
    elif (x <= 5):
        quadrantx = 2
    elif (x <= 8):
        quadrantx = 3
    
    if(y <= 2): #These conditions get the y value
        quadranty = 1
    elif (y <= 5):
        quadranty = 2
    elif (y <= 8):
        quadranty = 3
    
    if (quadrantx == 1): #These conditions get combine the x and y to get an overall quadrant, which is then returned
        if (quadranty == 1):
            quadrant = 1
        elif(quadranty == 2):
            quadrant = 4
        elif(quadranty == 3):
            quadrant = 7
            
    elif (quadrantx == 2):
        if (quadranty == 1):
            quadrant = 2
        elif(quadranty == 2):
            quadrant = 5
        elif(quadranty == 3):
            quadrant = 8
            
    elif (quadrantx == 3):
        if (quadranty == 1):
            quadrant = 3
        elif(quadranty == 2):
            quadrant = 6
        elif(quadranty == 3):
            quadrant = 9
    
    return quadrant
  
def getBounds(quadrant):
    '''
    The return value will be a 2x2 matrix:
        [
        [0,0],
        [0,0]
        ]
    Where the first set will be the bounds for the y and the second will be the bounds on the x.
    '''
    bounds = [[],[]]
    if ((quadrant == 1) | (quadrant == 4) | (quadrant == 7)):
        #print("test")
        bounds[1] = [0,2]
    elif ((quadrant == 2) | (quadrant == 5) | (quadrant == 8)):
        bounds[1] = [3,5]
    elif ((quadrant == 3) | (quadrant == 6) | (quadrant == 9)):
        bounds[1] = [6,8]
        
    if ((quadrant == 1) | (quadrant == 2) | (quadrant == 3)):
        bounds[0] = [0,2]
    elif ((quadrant == 4) | (quadrant == 5) | (quadrant == 6)):
        bounds[0] = [3,5]
    elif ((quadrant == 7) | (quadrant == 8) | (quadrant == 9)):
        bounds[0] = [6,8]
    #print("We Here\n{}\n{}\n".format(quadrant,bounds))
    return bounds
    
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
            
    if (len(checked[y][x]) == 1):
        board[y][x] = checked[y][x][0]
        #print(checked[y][x][0])
        checked[y][x] = []
    #Need to add conditions for when none of the values fit.
    #So when we need to go and recheck previous values
    #backTrack(board,location)
    
    return board


def CheckLengths(select):
    '''
    Checks the lengths of the arrays in checked.
    If select = 0:
        finds longest
        Returns the length
    elif select = 1:
        find shortest
        Returns the length and the location
    '''
    if (select == 0):
        length = 0
    elif(select == 1):
        length = [10,[]]
        
    for i in range(0,len(checked)):
            for j in range(0,len(checked[0])):
                if (select == 0): #Checks for longest
                    if (len(checked[i][j]) > length):
                        length = len(checked[i][j])
                        
                elif (select == 1): #Checks for shortest
                    if ((len(checked[i][j]) < length[0]) & (len(checked[i][j]) != 0)):
                        length = [len(checked[i][j]), [i,j]]
                    
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
        
        
        
        #CheckLengths() returns the longest length in the array of possible values.
        #Once they're all zeroed we have solved the Puzzle.
        length = CheckLengths(0)
        
        # print(length)
        # for i in checked:
        #      print(i)
        count += 1
        #print(count)
        if (count > 100):
            break
    if (length == 0):
        return boardCopy
    
    '''
    Now that we have done the obvious stuff, the following will be for more complex boards
    '''
    lengthStuff = [10,[]]
    count = 0
    while (lengthStuff[0] > 1):
        lengthStuff = CheckLengths(1) #Gets length of and location of shortest possibility
        #print("HERE:\n{}\n".format(lengthStuff))
        if(lengthStuff[0] == 1):
            boardCopy[lengthStuff[1][0]][lengthStuff[1][1]] = checked[lengthStuff[1][0]][lengthStuff[1][1]][0]
        else:
            pass
            
        
        count += 1
        if (count > 100):
            #print("test")
            break
    
    
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
