import time

def fibo_gen(max = None):
    n1, n2, counter = 0, 1, 0
    while not max or max >= n1:
        yield n1
        n1, n2 = n2, n1+n2
        
if __name__ == "__main__":
    fibonacci = fibo_gen(50)
    for elem in fibonacci:
        print(elem)
        time.sleep(0.05)