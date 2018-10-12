from memory_profiler import *
import sys

@profile
def factorial_re(x):
    return 1 if x == 0 else x * factorial_re(x-1)

if __name__ == '__main__':
   sys.setrecursionlimit(1000000)
   x = int(input())
   print(factorial_re(x))

import time
start_time = time.time()
factorial_re(x)
print("--- %s seconds ---" % (time.time() - start_time))