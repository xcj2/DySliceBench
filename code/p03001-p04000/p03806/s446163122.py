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

sys.setrecursionlimit(10000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input()


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
def slv(N, MA, MB, ABC):
    dp = defaultdict(lambda: defaultdict(
        lambda: defaultdict(lambda: sys.maxsize)))
    AB_MAX = N*10
    dp[0][0][0] = 0
    for i, (a, b, c) in enumerate(ABC):
        for j in range(AB_MAX):
            for k in range(AB_MAX):
                if not (i in dp and j in dp[i] and k in dp[i][j]):
                    continue
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][j+a][k+b] = min(dp[i+1][j+a][k+b], dp[i][j][k] + c)

    ans = sys.maxsize
    for a in dp[N]:
        if a == 0:
            continue
        for b in dp[N][a]:
            if b == 0:
                continue
            if a*MB == b*MA:
                ans = min(ans, dp[N][a][b])

    return ans if ans != sys.maxsize else -1


def main():
    N, MA, MB = read_int_n()
    ABC = [read_int_n() for _ in range(N)]

    print(slv(N, MA, MB, ABC))


if __name__ == '__main__':
    main()
