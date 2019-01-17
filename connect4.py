import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_SYMBOLS = ["1","2"]
EMPTY = "-"

def createBoard():
    board = []
    for row in range(ROW_COUNT):
        board.append([])
        for col in range(COLUMN_COUNT):
            board[row].append(EMPTY)
    return board


def printBoard(board):
    board = np.flip(board, 0)
    for row in board:
        rowStr = ""
        for col in row:
            rowStr += col + " "
        print(rowStr)


def getNextOpenRow(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r


def dropPiece(board, col, piece):
    row = getNextOpenRow(board, col)
    board[row][col] = piece


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


def menu():
    print("------Main Menu------")
    print()

    choice = input( """
                1: Play the Game
                2: Instructions
                3: Exit

    Please enter your choice (1,2,3): """)

    return choice


def isInt(s):
    try:
        int(s)
        return True
    except:
        return False


def takeTurn(board, turn):
    chosenCol = -1
    while chosenCol < 1 or chosenCol > COLUMN_COUNT:
        tmpChosenCol = input("Player "+PLAYER_SYMBOLS[turn]+", make your selection (1-"+str(COLUMN_COUNT)+"):")
        if isInt(tmpChosenCol):
            chosenCol = int(tmpChosenCol)
        else:
            print("Please enter a number.")
            chosenCol=-1
        if chosenCol >= 1 and chosenCol <= COLUMN_COUNT:
            if board[5][chosenCol-1] != EMPTY:
                chosenCol = -1
                print("Sorry but that column is full")

    col = chosenCol - 1 # this is the index of the column which is 1 less than the number they input

    dropPiece(board, col, PLAYER_SYMBOLS[turn])


def playGame():
    gameOver = False
    turn = 0
    board = createBoard()
    print()
    printBoard(board)

    while not gameOver:
        takeTurn(board, turn)
        if winningMove(board, PLAYER_SYMBOLS[turn]):
            print("Player "+PLAYER_SYMBOLS[turn]+" Wins!")
            printBoard(board)
            gameOver = True
        elif EMPTY in board[5]:
            #toggle the turn
            turn += 1
            turn = turn % 2
            print()
            printBoard(board)
        else:
            print("It's a draw!")
            gameOver = True


instructions = """

        This game is a spin off of the original game, Connect 4.
        It also incorporates aspects of Scrabble in that you place
        letters to make words and get points for every letter in
        every word that you make.

        The aim of the game is to get as many points as possible.
        You will be given a 'hand' of 7 randomly generated letters
        every turn. You can place up to 5 of these on one turn.
        You will gain points for every word that your letters on
        this turn helped to make. The letters in the words will
        account for one point each. The words made have to be at
        least 3 letters long. The winner is the player with the most
        points when the board is full.

        """


while True:
    choice = menu()
    if choice == "1":
        playGame()
    elif choice == "2":
        print(instructions)
    elif choice == "3":
        quit()
    else:
        print("You can only enter either 1, 2, or 3.")
        print("Please try again")
        menu()



#incorporate dictionary and words instead of pieces
#incorporate menu to include playing against computer- figure out strategy and how computer figures out how to place
#create a completely randomised hand
#check if words are created
#point system for words
