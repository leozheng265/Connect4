Connect 4 
=================

I created two versions of the connect 4 game. The first version is a simpler implementation. It asks the players to choose their moves by entering column numbers and displays the board as a 2-D array in the terminal. The second version is a more advanced version using pygame to visualize the board and user interaction.

In the simpler "verbose" implementation, I created a while loop that will keep asking the players to choose their moves until one of the terminal conditions is met. The function isTerminal takes in the board. It first checks if the board is full because it is the terminal condition for a tie. Then it divides the board into multiple blocks each containing four cells and I used the count function to check if there are four pieces from the same player which indicates the winner.

In the second implementation, the structure of the code is very similar but I added pygame functions to visualize the game board. The isTerminal function is also slightly different. Instead of returning a boolean value, it returns 1 if player 1 has won, 2 if player 2 has won, and 0 if there is a draw. The return value will be checked in the main program to decide if there is a winner.


### Branches
The main branch has the advanced implementation with visualization.
The verbose branch has the simplified implementation.
