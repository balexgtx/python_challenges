def consecutive_zeros(n):
    res = 0
    cons = 0
    for l in n:
        if l == "0":
            cons = cons + 1
        else:
            cons = 0
        res = max(res, cons)
    return res


def run():
    print(consecutive_zeros('10100101000'))


if __name__ == "__main__":
    run()