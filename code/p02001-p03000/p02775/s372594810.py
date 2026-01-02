# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = 2**62-1


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N):
    ans = 0
    M = N
    M = [c for c in M[::-1]]
    A = []
    M.append('0')
    carry = 0
    for i, c in enumerate(M):
        c = int(c) + carry
        carry = 0
        if c == 5 and int(M[i+1]) >= 5:
                carry += 1
                a = 0
        elif c >= 6:
            carry += 1
            a = 0
        else:
            a = c
        # A += 10**i * a
        A.append(a)
    # A += 10**(len(M)) * carry
    if carry != 0:
        A.append(carry)
    if A[-1] == 0:
        A.pop()
    A = ''.join(map(str, [c for c in A[::-1]]))

    if len(A) - len(N) > 0:
        N = ('0' * (len(A) - len(N))) + N

    carry = 0
    ans = 0
    for a, n in reversed(list(zip(A, N))):
        # print(a, n)
        a = int(a)
        ans += a
        n = int(n)
        if carry != 0:
            if a == 0:
                a = 9
                carry =1
            else:
                a -= 1
                carry = 0
        b = a - n
        if b < 0:
            b += 10
            carry = 1
        ans += b

    # print(N)
    # print(A)
    # B = int(A) - int(N)
    # for c in str(B):
    #     ans += int(c)
    # for c in str(A):
    #     ans += int(c)

    # print('   ', B)
    return ans


def main():
    N = read_str()
    print(slv(N))


if __name__ == '__main__':
    main()
