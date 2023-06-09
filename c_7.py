import time
from matplotlib import pyplot as plt
from tqdm import tqdm

import numpy as np
import numba as nb
@nb.njit('int64[:](int_)')
def collatz2(top_range):
    mem = np.zeros(top_range + 1, dtype=np.int64)
    for start in range(2, top_range + 1):
        # If mod(4) == 1: Value 2 or 3 Cached
        if start % 4 == 1:
            mem[start] = mem[(start + (start >> 1) + 1) // 2] + 3
        # If mod(4) == 3: Use Algorithm
        elif start % 4 == 3:
            num = start
            count = 0
            while num >= start:
                if num % 2:
                    num += (num >> 1) + 1
                    count += 2
                else:
                    num //= 2
                    count += 1
            mem[start] = mem[num] + count
        # If mod(4) == 2 or 4: Value 1 Cached
        else:
            mem[start] = mem[(start // 2)] + 1
    return mem


def collatz(top_range):
    mem = [0] * (top_range + 1)
    for start in range(2, top_range + 1):
        # If mod(4) == 1: Value 2 or 3 Cached
        if start % 4 == 1:
            mem[start] = mem[(start + (start >> 1) + 1) // 2] + 3
        # If mod(4) == 3: Use Algorithm
        elif start % 4 == 3:
            num = start
            count = 0
            while num >= start:
                if num % 2:
                    num += (num >> 1) + 1
                    count += 2
                else:
                    num //= 2
                    count += 1
            mem[start] = mem[num] + count
        # If mod(4) == 2 or 4: Value 1 Cached
        else:
            mem[start] = mem[(start // 2)] + 1
    return mem

# profiling here
def main():

    top_range = 100_000
    mem = collatz(top_range)
    mem2 = collatz2(top_range)
    assert np.allclose(np.array(mem), mem2)