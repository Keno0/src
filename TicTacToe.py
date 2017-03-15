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
    
def evaluate(dimension, board):
    counter = 0
    for i in range(dimension):
        for j in range(dimension-1):        
            if board[str(i)+str(j)] == board[str(i)+str(j+1)] and board[str(i)+str(j)] != ' ':
                counter += 1
                if(counter == 4):
                    if(board[str(i)+str(j+1)] == playerSymbol):
                        print('You won')
                    else:
                        print('You lose')
                    return True
            else:
                counter = 0
        counter = 0
            
    return False


         



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
AITurn = ''

print('Give indexes of column and row to put your symbol. Indexes are started from 0.')

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
    valid = False
    while valid != True:
        AITurn = str(random.randint(0,sizeOfBoard-1)) + str(random.randint(0,sizeOfBoard-1))
        print(AITurn)
        if(TicTacToeBoard[AITurn] != ' '):
            
            valid = False
        else:
            TicTacToeBoard[AITurn] = AISymbol
            valid = True
        
    printBoard(sizeOfBoard,TicTacToeBoard)
    
    endGame = evaluate(sizeOfBoard, TicTacToeBoard)
    




