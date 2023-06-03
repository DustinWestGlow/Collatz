import time

def collatz(x):
    while True:
        if x == 1:
            break
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1

times = []
num_tests = 10
for test in range(num_tests):
    start = time.time()
    for i in range(1, 10**5, 2):
        collatz(i)
    end = time.time()
    elapsed = end - start
    times.append(elapsed)
    # print(f"{elapsed:.5f}")
    print(test, end=" ")
print()
print(f"{num_tests} tests ran.")
avg_time = sum(times) / num_tests
print(f"Average time: {avg_time:.5f}")
print(times)