x = 15

while True:
    print(x)
    if x == 1:
        break
    if x % 2 == 0:
        x /= 2
    else:
        x = 3 * x + 1