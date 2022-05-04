import random

def check_position(matriz,n,m):
    if matriz[n][m] != "X" and matriz[n][m] != "O":
        return True
    else:
        return False


def win_condition(matriz,option):
    #fila x columna
    #Test Horizontal
    if matriz[0][0] == option and matriz[0][1] == option and matriz[0][2]  == option:
        return True
    elif matriz[1][0] == option and matriz[1][1] ==  option and matriz[1][2] == option:
        return True
    elif matriz[2][0] == option and matriz[2][1] == option and matriz[2][2] == option:
        return True
    #Test Vertical
    elif matriz[0][0] == option and matriz[1][0] == option and matriz[2][0] == option:
        return True
    elif matriz[0][1] == option and matriz[1][1] == option and matriz[2][1] == option:
        return True
    elif matriz[0][2] == option and matriz[1][2] == option and matriz[2][2] == option:
        return True
    #Diagonal
    elif matriz[2][0] == option and matriz[1][1] == option and matriz[0][2] == option:
        return True
    elif matriz[0][0] == option and matriz[1][1] == option and matriz[2][2] == option:
        return True
    else: 
        return False
    

def game():
    matriz = [['1','2','3'],
              ['4','5','6'],
              ['7','8','9']]
    #print(win_condition(matriz, 'X'))
    #print(matriz[0][1], matriz[1][1], matriz[2][1])
    #print(check_position(matriz, 0,0))
    #print(matriz[0][0])

def run():
    game()


if __name__ == "__main__":
    run()