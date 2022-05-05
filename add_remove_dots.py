from dataclasses import replace


def add_dots(strinx):
    new_strinx = '.'.join(strinx)
    return new_strinx


def remove_dots(strinx):
    new_strinx = strinx.replace('.','')
    return new_strinx


def run():
    pass

if __name__ == "__main__":
    run()