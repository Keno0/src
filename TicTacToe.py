import pprint
import random

print('Please give the size of the board.')
sizeOfBoard = int(input())
TicTacToeBoard = {}
playerSymbol = ''
AISymbol = ''

#get size of the board


#create board
def createBoard(dimension, board):
    for i in range(dimension):
        for j in range(dimension):
            board[str(i) + str(j)] = ' '
            
#print boards
def printBoard(dimension, board):
    for i in range(dimension):
        for j in range(dimension):
            if(j < dimension -1):
                print(board[str(i)+str(j)] + '|', end='' )
            else:
                print(board[str(i)+str(j)]) 
        
        if i < dimension -1 :
            for k in range(dimension*2 -1):
                print('-', end='')
            print()
    



         



createBoard(sizeOfBoard, TicTacToeBoard )

printBoard(sizeOfBoard, TicTacToeBoard)

#Choose a symbol
print('Please choose a symbol: press X or O and enter ')

while playerSymbol != 'O' and  playerSymbol != 'X':
    playerSymbol = input()
    if playerSymbol != 'O' and playerSymbol != 'X':
        print('Wrong symbol, please give me a right symbol.')
    
if playerSymbol == 'O':
    AISymbol = 'X'
else:
    AISymbol = 'O'

endGame = False
yourTurn = ''


while endGame != True:
    valid = False
    print('Your turn')
    while(valid != True):
        yourTurn = input()
        if(TicTacToeBoard[yourTurn] != ' '):
            print('That place is already selected.')
            valid = False
        else:
            TicTacToeBoard[yourTurn] = playerSymbol
            valid = True
    
    
    printBoard(sizeOfBoard,TicTacToeBoard)
    




