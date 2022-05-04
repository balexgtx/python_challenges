import random

def simulator():
    n = random.randint(1, 6)    
    if n == 1:
        print('''
            -----
            |   |
            | o |
            |   |
            -----
              ''')
    if n == 2:
        print(''' 
            -----
            |o  |
            |   |
            |  o|
            ----- ''')
    if n == 3:
        print('''
            -----
            |o  |
            | o |
            |  o|
            ----- 
              ''')
    if n == 4:
        print(''' 
            -----
            |o o|
            |   |
            |o o|
            -----
              ''')
    if n == 5:
        print('''
            -----
            |o o|
            | o |
            |o o|
            -----
              ''')
    if n == 6:
        print(''' 
            -----
            |o o|
            |o o|
            |o o|
            -----
              ''')
        
    
def run():
    simulator()


if __name__ == "__main__":
    run()