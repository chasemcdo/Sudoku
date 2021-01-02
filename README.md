# Sudoku
Repository for my Sudoku Game and Solver

This project sought to create a playable game of Sudoku which could also function as a solver.
The current implementation allows for one to play the game and have it solve the board, but doesn't allow for you to enter your own board to be solved.


How to use:
In the Sudoku.py file, you'll find all the "brains" behind the solving and computation.



The "AppInterface.py" file is where the interface is created. This file will call upon the Sudoku.py file to solve and check.
Currently AppInterface pulls the board pseudorandomly from "BoardBank.py", which may be updated in the future.
The plan for the future of Board generation is to create a generator that will create boards and add them to "BoardBank.py" for later use.
This implementation allows me to run the board generator, and store the boards to decrease run time for the user.

Getting the most out of this program will require pulling all three python files.

"Menu.py" is the file that you will run to get the "whole experience".
When run this file will bring up a menu that allows you to choose to start the game.

When in the game if you click the red button in the bottom right, you will be brought back to the menu.
