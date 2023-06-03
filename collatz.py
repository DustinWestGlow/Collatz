x = 15

while True:
    if x == 1:
        break
    if x % 2 == 0:
        x /= 2
    else:
        x = 3 * x + 1
    print(x)
    