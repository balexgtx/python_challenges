def is_anagram(strinx, strinxx):
    list1 = list(strinx)
    list2 = list(strinxx)
    list1.sort()
    list2.sort()
    return list1 == list2

def run():
    word = 'typhoon'
    word2    = 'opython'
    print(is_anagram(word, word2))

if __name__ == "__main__":
    run()