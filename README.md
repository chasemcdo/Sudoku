# Sudoku
Repository for my Sudoku Game and Solver

This project sought to create a playable game of Sudoku which could also function as a solver.
The current implementation allows for one to play the game and have it solve the board, but doesn't allow for you to enter your own board to be solved.


How to use:
In the Sudoku.py file, you'll find all the "brains" behind the solving and computation.


The "AppInterface.py" file is where the interface is created. This file will call upon the Sudoku.py file to solve and check.
Currently AppInterface pulls the "originalBoard" from Sudoku, but this may change in a future update and will be reflected in this document.

To run the program, you'll need to pull both "Sudoku.py" and "AppInterface.py".
Running "AppInterface.py" will initiate the gameboard where you'll have the ability to play the game and click the buttons at the bottom of the interface to do certain actions.
The currently available actions are:
Solve, Reset, Check, and Hint
