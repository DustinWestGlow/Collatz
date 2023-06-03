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

# {
#     "styles": ["simple", "fast", "cached"],
#     "data": [
#         {
#         "runs": "100",
#         "limit": "1000",
#         "times": [
#             {"elapsed": "1.061", "average": "0.011"},
#             {"elapsed": "", "average": ""},
#             {"elapsed": "", "average": ""}
#         ]
#     }, {
#         "runs": "",
#         "limit": "",
#         "times": []
#     }
#     ]
# }

# testing(100, 10**3)
# testing(1000, 1000)
# testing(100, 10**4)
# testing(10, 10**5)
# testing(4, 10**6)

class Runner(runs, limit):
    def __init__():
        self.runs = runs
        self.limit = limit
runners = [
    Runner(1000, 10**3),
    Runner(100, 10**4),
    Runner(10, 10**5),
    Runner(5, 10**6)
]
results = {}
styles = ["simple", "fast", "cached"]
results["styles"] = styles
results["data"] = []
for runner in runners:
    runs = runner["runs"]
    limit = runner["limit"]
    data = {
        "runs": runs,
        "limit": limit,
        "times": []
    }
    times = []
    for style in styles:
        times.append(testing(runs, limit, style))
    data["times"] = times
    results["data"].append(data)