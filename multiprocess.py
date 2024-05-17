from multiprocessing import Process, Queue, Lock, Pool
import time
import os

def factorial(n):
    return n*factorial(n-1) if n > 0 else 1

with Pool(processes=4) as pool:
    l = list([100 for _ in range(100000)])
    start = time.time()
    pool.map_async(factorial, l)
    print(time.time() - start)

    start = time.time()
    map(factorial, l)
    print(time.time() - start)
