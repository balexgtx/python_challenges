import random
# Randomness
# Define a function, random_number, that takes no parameters. 
# The function must generate a random integer between 1 and 100, both inclusive, and return it.

# Calling the function multiple times should (usually) return different numbers.

# For example, calling random_number() some times might first return 42, then 63, then 1.

def random_number():
    return random.randint(1,100)


def run():
    print(random_number())


if __name__ == "__main__":
    run()