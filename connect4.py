import numpy as np



ROWCOUNT = 6
COLUMNCOUNT = 7



def createBoard():
    board = np.zeros((ROWCOUNT, COLUMNCOUNT))
    return board



def dropPiece(board, row, col, player):
    print("row: ", row, "\ncol: ", col)
    board[row][col] = player

def validLocation(board, col):

    for i in range(0, ROWCOUNT):
        if board[i][col] == 0:
            return True
    print("The move your choose is invalid!!")
    return False


def getNextRow(board, col):
    
    for i in range(0, ROWCOUNT + 1):
        if board[i][col] == 0:
            return i

def printBoard(board):
    print(np.flip(board, 0))

def isTerminal(board):
    # check if the board is full
    empty = 42
    for i in range(ROWCOUNT):
        for j in range(COLUMNCOUNT):
            if not board[i][j] == 0:
                empty -= 1
    if(empty == 0):
        print("This game is a tie!\n")
        return True

        

    # check for horizontal terminal conditions
    for r in range(ROWCOUNT):
        rowArr = [i for i in list(board[r, :])]
        for c in range(0, 4):
            block = rowArr[c:c+4]
            if block.count(1) == 4:
                print("Player1 wins!!")
                return True
            if block.count(2) == 4:
                print("Player2 wins!!")
                return True

    # check for vertical terminal conditions
    for c in range(COLUMNCOUNT):
        colArr = [i for i in list(board[:, c])]
        for r in range(0, 3):
            block = colArr[r:r+4]
            if block.count(1) == 4:
                print("Player1 wins!!")
                return True
            if block.count(2) == 4:
                print("Player2 wins!!")
                return True

    # check for diagonal terminal conditions
    for c in range(0, 4):
        for r in range(0, 3):
            block = [board[r + i][c + i] for i in range(4)]
            if block.count(1) == 4:
                print("Player1 wins!!")
                return True
            if block.count(2) == 4:
                print("Player2 wins!!")
                return True

    for c in range(0, 4):
        for r in range(0, 3):

            block = [board[r + 3 - i][c + i] for i in range(4)]
            if block.count(1) == 4:
                print("Player1 wins!!")
                return True
            if block.count(2) == 4:
                print("Player2 wins!!")
                return True


    return False
    

    


print("Welcome to the Connect4 game\n")
print("Type numbers from 1 to 7 to choose your move\n")
print("You can exit the game by entering 0\n")

board = createBoard()
end = False
turn = 1
player = 1

while not end:
    if turn == 1:
        move = int(input("Player 1 is choosing the move (1-7) "))
        if move == 0:
            print(" \n")

            print("Exiting...\n")
            print("Bye")

            break
        move -= 1
        while move > COLUMNCOUNT - 1:
            print("Invalide Column Number\n")
            move = int(input("Please choose your move again (1-7) "))
            move -= 1
        if validLocation(board, move):
            row = getNextRow(board, move)
            dropPiece(board, row, move, player)
            printBoard(board)

        end = isTerminal(board)

        player += 1

    else:
        move = int(input("Player 2 is choosing the move (1-7) "))
        if move == 0:
            print(" \n")
            print("Exiting...\n")
            print("Bye")
            break
        move -= 1
        while move > COLUMNCOUNT - 1:
            print("Invalide Column Number\n")
            move = int(input("Please choose your move again (1-6) "))
            move -= 1
        if validLocation(board, move):
            row = getNextRow(board, move)
            dropPiece(board, row, move, player)
            printBoard(board)

        end = isTerminal(board)

        player -= 1



    turn += 1
    turn %= 2

