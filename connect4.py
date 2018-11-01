import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def createBoard():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece

def isValidLocation(board, col):
    return board[COLUMN_COUNT-1][col] == 0

def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(np.flip(board, 0))

def winningMove(board, piece):
    #Check horizontal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #Check negatively sloped diaganols
    for c in range(COLUMN_COUNT):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = createBoard()
printBoard(board)
gameOver = False
turn = 0

while not gameOver:
    #Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1, make your selection (0-6):"))

        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)

            if winningMove(board, 1):
                print("Player 1 Wins!")
                gameOver = True



    #Ask for Player 2 Input
    else:
        col = int(input("Player 2, make your selection (0-6):"))

        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)

            if winningMove(board, 2):
                print("Player 2 Wins!")
                gameOver = True

    printBoard(board)

    turn += 1
    turn = turn % 2
