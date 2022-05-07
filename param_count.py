from ast import arguments


def param_count(*arguments):
    return arguments.__len__()

def run():
    print(param_count('one', 'two', 'three', 'four'))

if __name__ == "__main__":
    run()