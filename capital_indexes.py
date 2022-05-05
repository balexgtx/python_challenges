def capita_indexes(s):
    char_indexes = []
    for i, l in enumerate(s):
        if l.isupper():
            char_indexes.append(i)
    return char_indexes

def run():
    s = 'HolaCaMArAdA'
    result = capita_indexes(s)
    print(result)


if __name__ == "__main__":
    run()
