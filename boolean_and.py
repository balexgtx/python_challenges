# Boolean and
#Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.


def triple_and(a,b,c):
    if a == True and b == True and c == True:
        return True
    else:
        return False

def triple_and2(a,b,c):
    return a and b and c


def run():
    print(triple_and(True, True, True))
    print(triple_and2(True, True, True))
    print(triple_and(False, True, True))
    print(triple_and2(False, True, True))



if __name__ == "__main__":
    run()