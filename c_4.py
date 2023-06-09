import time

def collatz(x):
    while True:
        if x == 1:
            break
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1

def testing(num_tests, limit):
    times = []
    print("Running: ", end='')
    for test in range(num_tests): # num_tests
        start = time.time()
        for i in range(1, limit, 2): # limit
            collatz(i)
        end = time.time()
        elapsed = end - start
        times.append(elapsed)
        print('.', end="")
    print()
    total_time = sum(times)
    avg_time = total_time / num_tests
    print(f"Ts:{num_tests}, Lt:'{limit}', El:{total_time:.5f}, Av:{avg_time:.5f}")

testing(100, 10**3)
testing(40, 10**4)
testing(10, 10**5)
# testing(4, 10**6)