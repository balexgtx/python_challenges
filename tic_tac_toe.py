import random


def printBoard(board):
    print(f'''
         {board[0]} | {board[1]} | {board[2]}
        -----------
        
         {board[3]} | {board[4]} | {board[5]}
        -----------
        
         {board[6]} | {board[7]} | {board[8]}
        ''')


def check_position(board,pos):
    if board[pos] != "X" or board[pos] != "O":
        return True
    else:
        False


def write_position(board, pos, ob):
    if check_position(board,pos) == True:
        board[pos] == ob
        return True
    else:
        return False


def check_victory(board):
    #Horizontal
    if board[0] == board[1] and board[2] == board[1]:
        return True
    elif board[3] == board[4] and board[5] == board[3]:
        return True
    elif board[6] == board[7] and board[8] == board[6]:
        return True
    #Vertical
    elif board[0] == board[3] and board[6] == board[0]:
        return True
    elif board[1] == board[4] and board[7] == board[1]:
        return True
    elif board[2] == board[5] and board[8] == board[2]:
        return True
    #Diagonal
    elif board[0] == board[4] and board[8] == board[0]:
        return True
    elif board[6] == board[4] and board[2] == board[6]:
        return True
    else:
        return False


def game():
    board = ['1','2','3','4','5','6','7','8', '9']
    #print(board)
    print('Juego iniciado!...')
    print('El usuario coloca X!')
    print('La computadora juega con O!')
    printBoard(board)
    #print(check_victory(board))
    while check_victory != True:
        try:
            print('Donde quieres colocar X!: ')
            user_movement = int(input())
        except ValueError:
            print('Ingresa datos validos! ')
    else:
        pass
    
    
def run():
    game()


if __name__ == "__main__":
    run()