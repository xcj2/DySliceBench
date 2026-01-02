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


def get_inputs(cast_func=None):
    if cast_func is None:
        return input().split()
    else:
        return list(map(cast_func, input().split()))


def get_input(cast_func=None):
    if cast_func is None:
        return input()
    else:
        return cast_func(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    N = get_input(int)
    A = np.zeros((10, 10), dtype=np.int32)
    for i in range(1, N+1):
        A[int(str(i)[0]), int(str(i)[-1])] += 1

    # print(A.sum())
    # print(A)
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += A[i, j] * A[j, i]

    print(ans)

    return


if __name__ == '__main__':
    main()
