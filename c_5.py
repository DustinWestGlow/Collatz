cache = {1}

def collatz(x):
    starter = x
    while True:
        if x in cache:
            print()
            break
        print(int(x), end=' ')
        cache.add(x)
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1

for i in range(1, 20):
    collatz(i)