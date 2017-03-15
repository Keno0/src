import pprint

#get size of the board
print('Please give the size of the board.')
sizeOfBoard = int(input())
TicTacToeBoard = {}

#create board
def createBoard(dimension, board):
    for i in range(dimension):
        for j in range(dimension):
            board[str(i) + str(j)] = ' '
            

createBoard(sizeOfBoard, TicTacToeBoard )        

pprint.pprint(TicTacToeBoard)