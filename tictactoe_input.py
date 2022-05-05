def get_row_col(i):
    lista = list(i)
    row = ''
    col = ''
    if lista[0] == 'A':
        col = 0
    elif lista[0] == 'B':
        col = 1
    elif lista[0] == 'C':
        col = 2
    
    if lista[1] == '1':
        row = 0
    elif lista[1] == '2':
        row = 1
    elif lista[1] == '3':
        row = 2
    
    return (col,row)

def run():
    print(get_row_col('A1'))


if __name__ == "__main__":
    run()