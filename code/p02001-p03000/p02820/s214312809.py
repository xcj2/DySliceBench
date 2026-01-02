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
    # A, B, K = get_inputs(int)
    # if A >= K:
    #     print(A-K, B)
    # elif A + B >= K:
    #     print(0, B - (K-A))
    # else:
    #     print(0, 0)

    # N = get_input(int)
    # n = X
    # while True:
    #     if is_prime(n):
    #         print(n)
    #         return
    #     else:
    #         n += 1

    N, K = get_inputs(int)
    R, S, P = get_inputs(int)
    T = get_input()

    points = {'r': R, 's': S, 'p': P}
    towin = {'r': 'p', 's': 'r', 'p': 's'}
    todraw = {'r': 'r', 's': 's', 'p': 'p'}

    ret = ''
    score = 0
    for i in range(N):
        if i < K:
            choice = towin[T[i]]
            ret += choice
            score += points[choice]
        else:
            if ret[-K] != towin[T[i]]:
                choice = towin[T[i]]
                ret += choice
                score += points[choice]
            else:
                choices = set(['r', 's', 'p'])
                choices -= set([ret[-K],])
                if i + K < len(T):
                    choices -= set([towin[T[i+K]],])
                choice = list(choices)[0]
                ret += choice


    print(score)


if __name__ == '__main__':
    main()
