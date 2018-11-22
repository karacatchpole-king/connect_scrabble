import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_SYMBOLS = ["1","2"]
EMPTY = "0"

def createBoard():
    board = []
    for row in range(ROW_COUNT):
        board.append([])
        for col in range(COLUMN_COUNT):
            board[row].append(EMPTY)
    return board

#could be linked with invalid and isInvalidPiece?
# def isValidLocation(board, col):
#     return board[ROW_COUNT-1][col] == 0

def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r
def dropPiece(board, col, piece):
    row = getNextOpenRow(board, col)
    board[row][col] = piece

def printBoard(board):
    print(np.flip(board, 0))

def winningMove(board, piece):
    #check horizontal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #check negatively sloped diagonals
    for c in range(COLUMN_COUNT):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
#
# def isInvalidPiece(board, col, piece):
#     if piece <1 or piece >COLUMN_COUNT:
#         print ("Invalid Placement")
#         return True

def takeTurn(player, board):
    chosenCol = -1
    while chosenCol < 1 or chosenCol > COLUMN_COUNT:
        chosenCol = int(input("Player "+PLAYER_SYMBOLS[turn]+", make your selection (1-"+str(COLUMN_COUNT)+"):"))
        if chosenCol >= 1 and chosenCol <= COLUMN_COUNT:
            if board[0][chosenCol-1] != EMPTY:
                chosenCol = -1
                print("Sorry but that column is full") #this message is currently displayed when a player is trying to put their piece in the second row

    col = chosenCol - 1 # this is the index of the column which is 1 less than the number they input

    dropPiece(board, col, PLAYER_SYMBOLS[turn])



board = createBoard()
printBoard(board)
gameOver = False
turn = 0
#invalid = True

while not gameOver:
    takeTurn(turn, board)
    if winningMove(board, PLAYER_SYMBOLS[turn]):
        print("Player "+PLAYER_SYMBOLS[turn]+" Wins!")
        gameOver = True
    elif EMPTY in board[0]:
        #toggle the turn
        turn += 1
        turn = turn % 2
    else:
        print("It's a draw!")
        gameOver = True


    printBoard(board)


#incorporate dictionary and words instead of pieces
#incorporate menu to include playing against computer- figure out strategy and how computer figures out how to place
#create a completely randomised hand
#check if words are created
