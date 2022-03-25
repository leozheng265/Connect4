import pygame
import numpy as np
import sys
import math

PLAYER1 = 1
PLAYER2 = 2
ROWCOUNT = 6
COLUMNCOUNT = 7
SCREENSIZE = 140
RADIUS = (SCREENSIZE/2 - 5)
ORANGE = (255, 128, 0)
BLACK = (0, 0, 0)
BLUE = (145, 60, 255)
YELLOW = (255, 255, 0)


def createBoard():
    board = np.zeros((ROWCOUNT, COLUMNCOUNT))
    return board



def dropPiece(board, row, col, player):
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
        return 0

    # check for horizontal terminal conditions
    for r in range(ROWCOUNT):
        rowArr = [i for i in list(board[r, :])]
        for c in range(0, 4):
            block = rowArr[c:c+4]
            if block.count(PLAYER1) == 4:
                print("Player1 wins!!")
                return PLAYER1
            if block.count(PLAYER2) == 4:
                print("Player2 wins!!")
                return PLAYER2

    # check for vertical terminal conditions
    for c in range(COLUMNCOUNT):
        colArr = [i for i in list(board[:, c])]
        for r in range(0, 3):
            block = colArr[r:r+4]
            if block.count(PLAYER1) == 4:
                print("Player1 wins!!")
                return PLAYER1
            if block.count(PLAYER2) == 4:
                print("Player2 wins!!")
                return PLAYER2

    # check for diagonal terminal conditions
    for c in range(0, 4):
        for r in range(0, 3):
            block = [board[r + i][c + i] for i in range(4)]
            if block.count(PLAYER1) == 4:
                print("Player1 wins!!")
                return PLAYER1
            if block.count(PLAYER2) == 4:
                print("Player2 wins!!")
                return PLAYER2

    for c in range(0, 4):
        for r in range(0, 3):
            block = [board[r + 3 - i][c + i] for i in range(4)]
            if block.count(PLAYER1) == 4:
                print("Player1 wins!!")
                return PLAYER1
            if block.count(PLAYER2) == 4:
                print("Player2 wins!!")
                return PLAYER2
    return 0
    

def drawBoard(board):
    for r in range(ROWCOUNT):
        for c in range(COLUMNCOUNT):
            pygame.draw.rect(screen, BLUE, (c * SCREENSIZE, (r + 1) * SCREENSIZE, SCREENSIZE, SCREENSIZE))
            pygame.draw.circle(screen, BLACK, ((c + 0.5) * SCREENSIZE, (r + 1.5) * SCREENSIZE), RADIUS)
    
    for r in range(ROWCOUNT):
        for c in range(COLUMNCOUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, ORANGE, ((c + 0.5) * SCREENSIZE, height - (r + 0.5) * SCREENSIZE), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, ((c + 0.5) * SCREENSIZE, height - (r + 0.5) * SCREENSIZE), RADIUS)
    pygame.display.update()

board = createBoard()
end = False
turn = 1
player = 1

# initialize pygame
pygame.init()

# set up the board to display
height = SCREENSIZE * (ROWCOUNT + 1)
width = SCREENSIZE * COLUMNCOUNT
size = (width, height)
screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

font = pygame.font.SysFont("monospace", 90)


while not end:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SCREENSIZE))
            posx = event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen, ORANGE, (posx, SCREENSIZE/2), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, SCREENSIZE/2), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SCREENSIZE))

            if turn == 1:
                posx = event.pos[0]
                move = math.floor(posx/SCREENSIZE)
                
                if validLocation(board, move):
                    row = getNextRow(board, move)
                    dropPiece(board, row, move, player)

                if isTerminal(board) == 1:
                    label = font.render("Player 1 has won!!!", 1, ORANGE)
                    screen.blit(label, (40, 10))
                    end = True

                player += 1

            else:
                posx = event.pos[0]
                move = math.floor(posx/SCREENSIZE)

                if validLocation(board, move):
                    row = getNextRow(board, move)
                    dropPiece(board, row, move, player)


                if isTerminal(board) == 2:
                    label = font.render("Player 2 has won!!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    end = True

                player -= 1
            
            printBoard(board)
            drawBoard(board)

            turn += 1
            turn %= 2

            if end:
                pygame.time.wait(4000)

