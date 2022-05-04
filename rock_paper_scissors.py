import random
import re



def item_choice(the_choice):
    if the_choice == 1:
        return 'Piedra'
    if the_choice == 2:
        return 'Papel'
    if the_choice == 3:
        return 'Tijeras'


#if we return true, user gonna win, if we return false, computer wins
def win_condition(user, computer):
    if user == 'Piedra' and computer == 'Tijeras':
        return True
    if user == 'Papel' and computer == 'Piedra':
        return True
    if user == 'Tijeras' and computer == 'Papel':
        return True
    if user == 'Tijeras' and computer == 'Piedra':
        return False
    if user == 'Piedra' and computer == 'Papel':
        return False
    if user == 'Papel' and computer == 'Tijeras':
        return False


def game():
            #We use random to select a random int between 1 and 3
    computer_random = random.randint(1,3)
            #We use our item_choice function to get the real item
    computer_choice = item_choice(computer_random)
            #We use our item_choice function to get the real item
    while True:
        try:
            user_number = int(input('''Selecciona que jugaras!: 
            1. Piedra
            2. Papel
            3. Tijeras
            '''))
            user_choice = item_choice(user_number)
            if user_number <= 0 or user_number > 3:
                raise ValueError
            if computer_choice == user_choice:
                print('Ha sido un empate...!')
                exit()
            else:
                result = win_condition(user_choice, computer_choice)
                if result == True:
                    print('Feliciades usuario! has ganado! ')
                    print('usuario: ' + user_choice, ' Computadora: ', computer_choice)
                    exit()
                else:
                    print('La computadora ha ganado! ')
                    print('usuario: ' + user_choice, ' Computadora: ', computer_choice)
                    exit()
        except ValueError:
            print('Error ejejejjeje')

def run():
    game()


if __name__ == "__main__":
    run()