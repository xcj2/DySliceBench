import collections
import math
import operator as op
from functools import reduce
import numpy as np
import math
import bisect
import heapq


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def get_inputs(cast_func=int):
    return list(map(cast_func, input().split()))


def get_input(cast_func=int):
    return cast_func(input())


def main():
    N, M = get_inputs()
    A = get_inputs()

    max_heap = [-a for a in A]
    heapq.heapify(max_heap)
    while M > 0:
        a_max = -heapq.heappop(max_heap)
        a_max //= 2
        heapq.heappush(max_heap, -a_max)
        M -= 1

    ans = -sum(max_heap)
    print(ans)


if __name__ == '__main__':
    main()
