def all_equal(l):
   return not l or l.count(l[0]) == len(l)

def run():
    l = [1,1,1,1]
    print(all_equal(l))
    print(len(l))


if __name__ == "__main__":
    run()