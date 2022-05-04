import random

def check_position(matriz,n,m):
    if matriz[n][m] != "X" and matriz[n][m] != "O":
        return True
    else:
        return False

#fila x columna
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
    

def print_matriz(matriz):
    print(f'''
         {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}
        -----------
        
         {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]}
        -----------
        
         {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]}
        ''')


def convert_choice_into_position(n):
    if n == 1:
        x = 0
        y = 0
        return x,y
    elif n == 2:
        x = 0
        y = 1
        return x,y
    elif n == 3:
        x = 0
        y = 2
        return x, y
    elif n == 4:
        x = 1
        y = 0
        return x, y
    elif n == 5:
        x = 1
        y = 1
        return x, y
    elif n == 6:
        x = 1
        y = 2
        return x, y
    elif n == 7:
        x = 2
        y = 0
        return x, y
    elif n == 8:
        x = 2
        y = 1
        return x, y
    elif n == 0:
        x = 2
        y = 2
        return x, y
    


def game():
    matriz = [['1','2','3'],
              ['4','5','6'],
              ['7','8','9']]
    #print(win_condition(matriz, 'X'))
    #print(matriz[0][1], matriz[1][1], matriz[2][1])
    #print(check_position(matriz, 0,0))
    #print(matriz[0][0])
    print('El juego ha comenzado!')
        #computer_position_x = random.randint(0,2)
    #print(computer_position_x)
        #computer_position_y = random.randint(0,2)
    #print(computer_position_y)
    
    #user_x = int(input('Ingresa la coordenada X: '))
    #user_y = int(input('Ingresa la coordenada Y: '))
    #print(print_matriz(matriz))
    print_matriz(matriz)
    n = int(input('Ingresa el numero al que quieres mover tu ficha!: '))
    a = convert_choice_into_position(n)
    print(matriz[a[0]][a[1]])
    
    
    
    

def run():
    game()


if __name__ == "__main__":
    run()