import time

def collatz(x, style):
    if style == "simple":
        while True:
            if x == 1:
                break
            if x % 2 == 0:
                x /= 2
            else:
                x = 3 * x + 1
    elif style == "fast":
        while True:
            if x == 1:
                break
            if x % 2 == 0:
                x /= 2
            else:
                x = 3 * x + 1
    elif style == "cached":
        while True:
            if x == 1:
                break
            if x % 2 == 0:
                x /= 2
            else:
                x = 3 * x + 1
    

def testing(num_tests, limit, style):
    times = []
    print("Running: ", end='')
    for test in range(num_tests): # num_tests
        start = time.time()
        for i in range(1, limit, 2): # limit
            collatz(i, style)
        end = time.time()
        elapsed = end - start
        times.append(elapsed)
        print('.', end="")
    print()
    total_time = sum(times)
    avg_time = total_time / num_tests
    print(f"Ts:{num_tests}, Lt:'{limit}', El:{total_time:.5f}, Av:{avg_time:.5f}")
    return {
        "elapsed": total_time,
        "average": avg_time
    }

# {
#     "styles": ["simple", "fast", "cached"],
#     "runs": [
#         { "cycles": "100", "limit": "1000" },
#         { "cycles": "30", "limit": "10000" },
#         { "cycles": "4", "limit": "100000" }
#     ],
#     "data": [
#         [
#             {"elapsed": "1.061", "average": "0.011"},
#             {"elapsed": "", "average": ""},
#             {"elapsed": "", "average": ""}
#         ],
#         [
#             {"elapsed": "", "average": ""}
#         ]
#     ]
# }

styles = ["simple", "fast", "cached"]
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
# for run in runs:
#     cycles = run["cycles"]
#     limit = run["limit"]
#     times = []
#     for style in styles:
#         times.append(testing(cycles, limit, style))
#     results["data"].append(times)
