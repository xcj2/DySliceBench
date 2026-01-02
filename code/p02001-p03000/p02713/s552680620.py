import sys
input = sys.stdin.readline
from itertools import *
from functools import *
from collections import *
from heapq import heapify, heappop, heappush, heappushpop
import math

INF = float('inf')
NIL = - 1

import time
from functools import wraps


def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start
        print(f'{elapsed_time} [ms]')
        return result

    return wrapper


def gcd(a, b):
    """
    Greatest Common Divisor
    Euclidean Algortihm
    """
    if a < b:
        gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    m = math.floor(math.sqrt(n)) + 1
    for p in range(3, m, 2):
        if n % p == 0:
            return False
    return True


def main():
    K = int(input())
    num_list = range(1, K + 1)

    total = 0

    for a in range(1, K + 1):
        if a == 1:
            total += K ** 2
            continue
        for b in range(1, K + 1):
            if b == 1:
                total += K
                continue
            tmp = gcd(a, b)
            if tmp == 1:
                total += K
                continue
            tmp_b = is_prime(tmp)
            for c in range(1, K + 1):
                if c == 1:
                    total += 1
                    continue
                if tmp_b:
                    if c % tmp == 0:
                        total += tmp
                        continue
                    else:
                        total += 1
                        continue
                else:

                # print(a, b, c)
                # print(gcd(tmp, c))
                    total += gcd(tmp, c)
    print(total)


if __name__ == '__main__':
    main()
