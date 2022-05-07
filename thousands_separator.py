import numbers


def format_number(n: int):
    n_string = str(format(n, ',d'))
    return n_string
    #print(n_string, round(n_commas))

def run():
    print(format_number(1200000))

if __name__ == "__main__":
    run()