import random

numero_aleatorio = random.randint(1,100)

def game():
    while True:
        try:
            numero_usuario = int(input('Ingresa un numero!: '))
            while numero_aleatorio != numero_usuario:
                if numero_usuario > numero_aleatorio:
                    numero_usuario = int(input('Ingresa un numero menor!: '))
                elif numero_usuario < numero_aleatorio:
                    numero_usuario =  int(input('Ingresa un numero mayor!: '))
            else:
                print('Has ganado!')
        except ValueError:
            print("Debes ingresar un numero! ")

def run():
    game()

if __name__ == "__main__":
    run()