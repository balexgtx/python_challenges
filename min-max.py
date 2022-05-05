def largest_difference(lista):
    largest = max(lista)
    mini = min(lista)
    return largest - mini


def run():
    lista = [1,2,40,100,2]
    print(largest_difference(lista))
    

if __name__ == "__main__":
    run()