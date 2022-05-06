def zap(a,b):
    res = []
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                res.append((a[i],b[j]))
    return res

def run():
    a = [1,3,5,7]
    b = [2,4,6,8]
    print(zap(a,b))


if __name__ == "__main__":
    run()