# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. 
# For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. The parameter is a string. 
# Your function must return True if there are two identical letters in a row in the string, and False otherwise.

from operator import truediv


def double_letters(strinx):
    for i in range(len(strinx)-1):
        if strinx[i] ==  strinx[i+1]:
            return True
    return False


def run():
    print(double_letters('Hello'))


if __name__ == "__main__":
    run()