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
    { "cycles": 30, "limit": 10000 },
    { "cycles": 4, "limit": 100000 }
]
results = {}
results["styles"] = styles
results["runs"] = runs
results["data"] = []
for style in styles:
    times = []
    for run in runs:
        cycles = run["cycles"]
        limit = run["limit"]
        times.append(testing(cycles, limit, style))
    results["data"].append(times)
print(results)
