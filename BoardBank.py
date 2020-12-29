# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:40:17 2020

This is the bank of boards used for pseudorandom generation of the gameboard.
I may create an actual random board generator so that there can be many more boards,
but that kind of negates the original point of this project which was creating the Sudoku Solver.

This is because the best way I have found to create random boards is to take a random filled board
and remove numbers at random such that there still exits one unique solution to the board and
stop removing numbers once doing so would result in more than one solution.

This makes the solver redundant, as we would have the complete board from the beginning in this case.

@author: chase
"""

board =     [[#Board 0
            [0,7,0,0,4,2,0,0,3],
            [0,0,2,0,9,0,0,0,5],
            [0,0,8,0,0,0,1,0,0],
            [0,0,0,0,8,0,6,0,2],
            [7,1,0,0,0,0,0,4,8],
            [2,0,6,0,5,0,0,0,0],
            [0,0,7,0,0,0,4,0,0],
            [1,0,0,0,7,0,8,0,0],
            [5,0,0,9,6,0,0,1,0]
            ],
#board1
[
            [9,1,0,3,4,0,0,0,7],
            [0,8,3,0,9,7,0,5,0],
            [4,2,7,0,0,0,0,1,0],
            [0,0,2,6,8,0,4,0,0],
            [7,0,4,2,0,9,0,0,0],
            [0,0,8,0,3,4,1,6,0],
            [8,0,0,0,0,0,0,4,0],
            [0,0,9,0,0,0,7,2,6],
            [0,5,6,0,0,3,8,0,1]
            ],
#board2
[
            [8,0,0,0,5,2,0,4,0],
            [7,0,0,0,0,0,0,8,1],
            [0,4,5,0,7,8,0,9,6],
            [0,0,0,0,6,0,1,0,0],
            [0,6,2,8,9,5,3,7,0],
            [4,7,0,0,3,1,0,0,0],
            [9,1,3,7,0,4,0,5,8],
            [0,0,7,0,0,0,0,3,2],
            [0,0,0,0,8,6,0,0,0]
            ]
#board3
# [
            # [0,0,0,0,0,0,0,0,0],
            # [0,0,0,0,0,0,0,0,0],
            # [0,0,0,0,0,0,0,0,0],
            # [0,0,0,0,0,0,0,0,0],
            # [0,0,0,0,0,0,0,0,0],
            # [0,0,0,0,0,0,0,0,0],
            # [0,0,0,0,0,0,0,0,0],
            # [0,0,0,0,0,0,0,0,0],
            # [0,0,0,0,0,0,0,0,0]
#             ],
# #Board4
# [
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,0,0,0]
#             ]
]