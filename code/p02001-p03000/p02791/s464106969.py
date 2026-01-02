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
    # a, b = get_inputs(int)
    # A = str(a)*b
    # B = str(b) * a
    # if A < B:
    #     print(A)
    # else:
    #     print(B)
    N = get_input(int)
    P = get_inputs(int)

    P_min = None
    ans = 0
    for i in range(N):
        if P_min is None:
            ans += 1
            P_min = P[i]
            continue

        if P[i] <= P_min:
            ans += 1

        P_min = min(P_min, P[i])
    # print(' '.join(map(str, ans)))
    print(ans)

    return


if __name__ == '__main__':
    main()
