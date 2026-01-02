import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions

import copy

# import heapq
# from collections import deque
# import decimal

sys.setrecursionlimit(10000001)
INF = sys.maxsize
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))


# ===CODE===


def main():
    def euclid(a, b):
        if b == 0:
            return a
        else:
            return euclid(b, a % b)

    def multiple(a, b):
        return a * b // euclid(a, b)

    n, m = ns()
    s = list(input())
    t = list(input())

    gcd = multiple(n, m)

    s_idx = [gcd // n * i for i in range(n)]
    t_idx = [gcd // m * i for i in range(m)]
    t_set = set(t_idx)

    for idx in s_idx:
        if idx in t_set:
            if s[idx * n // gcd] != t[idx * m // gcd]:
                print(-1)
                exit(0)

    print(gcd)


if __name__ == '__main__':
    main()
