from memory_profiler import *

@profile
def factorial(x):
    if type(x) != int:
        raise TypeError("Некорректный ввод")
    if x < 0:
        raise Exception("Некорректный ввод")
    thing = 1
    for i in range(1, x + 1):
        thing *= i
    return thing

if __name__ == '__main__':
    x = int(input())
    print(factorial(x))

import time
start_time = time.time()
factorial(x)
print("--- %s seconds ---" % (time.time() - start_time))