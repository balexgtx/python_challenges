def online_count(dic):
    n = 0
    for status in dic.values():
        if status == 'online':
            n = n + 1
    return n


def run():
    statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    }   
    
    print(online_count(statuses))

if __name__ == "__main__":
    run()