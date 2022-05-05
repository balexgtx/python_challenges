def mid(strinx):
    l = len(strinx) % 2
    if l == 0:
        return ''
    elif l != 0:
        strinx_mid = len(strinx) // 2
        return strinx[strinx_mid]


def run():
    print(mid("abcde"))
    

if __name__ == "__main__":
    run()