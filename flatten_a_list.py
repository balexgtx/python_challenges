def flatten(lista):
    return [item for sublist in lista for item in sublist]


def run():
    a = [1,2,3,[5,6,7]]
    print(flatten(a))
    

if __name__ == "__name__":
    run()