import time

def testing(num_tests, limit, style):
    times = []
    print("Running: ", end='')
    for test in range(num_tests): # num_tests
        start = time.time()
        if style == "original":
            for i in range(1, limit, 2): # limit
                x = i
                while True:
                    if x == 1:
                        break
                    if x % 2 == 0:
                        x /= 2
                    else:
                        x = 3 * x + 1
        elif style == "fast":
            cache = {1}
            for i in range(1, limit, 2): # limit
                x = i
                while True:
                    if x in cache:
                        break
                    else:
                        cache.add(x)
                    if x % 2 == 0:
                        x /= 2
                    else:
                        x = (3 * x + 1) / 2
        end = time.time()
        elapsed = end - start
        times.append(elapsed)
    # /num_tests
    total_time = sum(times)
    avg_time = total_time / num_tests
    print(f"Ts:{num_tests}, Lt:'{limit}', El:{total_time:.5f}, Av:{avg_time:.5f}")
    return {
        "elapsed": total_time,
        "average": avg_time
    }

styles = ["original", "fast"]
runs = [
    { "cycles": 100, "limit": 1000 },
    { "cycles": 10, "limit": 10000 },
    { "cycles": 1, "limit": 100000 }
]
data = []
for style in styles:
    times = []
    for run in runs:
        cycles = run["cycles"]
        limit = run["limit"]
        times.append(testing(cycles, limit, style))
    data.append(times)


for i, times in enumerate(data):
    print(styles[i].upper())
    for j, t in enumerate(times):
        r = runs[j]
        cycles = r["cycles"]
        limit = r["limit"]
        elapsed = t["elapsed"]
        benchmark_string = f"{(cycles * limit / (10**6) / elapsed):.4f} MegaCycles/Sec"
        print(str(cycles) + "C@" + str(limit) + "L" + "\t" + benchmark_string)