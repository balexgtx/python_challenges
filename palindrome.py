def palindrome(s):
    return s == s[::-1]


def run():
    print(palindrome('ana'))
    

if __name__ == "__main__":
    run()