# Define a function named list_xor. Your function should take three parameters: n, list1 and list2.

# Your function must return whether n is exclusively in list1 or list2.

# In other words, if n is in both lists or in none of the lists, return False. If n is in only one of the lists, return True.

# For example:

def list_xor(n, list1, list2):
    if list1.__contains__(n) and list2.__contains__(n):
        return False
    elif list1.__contains__(n) and list2.__contains__(n) == False:
        return True
    elif list1.__contains__(n) == False and list2.__contains__(n):
        return True
    elif list1.__contains__(n) == False and list2.__contains__(n) == False:
        return False
    
def list_xor2(n, list1, list2):
    return (n in list1) ^ (n in list2)

def run():
    print(list_xor(1, [1, 2, 3], [4, 5, 6]))
    print(list_xor(1, [0, 2, 3], [1, 5, 6]))
    print(list_xor(1, [1, 2, 3], [1, 5, 6]))
    print(list_xor(1, [0, 0, 0], [4, 5, 6]))
    
    print(list_xor2(1, [1, 2, 3], [4, 5, 6]))
    print(list_xor2(1, [0, 2, 3], [1, 5, 6]))
    print(list_xor2(1, [1, 2, 3], [1, 5, 6]))
    print(list_xor2(1, [0, 0, 0], [4, 5, 6]))


if __name__ == "__main__":
    run()