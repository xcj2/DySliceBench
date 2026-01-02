from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from functools import lru_cache, reduce
from math import ceil, floor
from sys import setrecursionlimit

import heapq
import itertools
import operator


inf = float('inf')


# globals
N = ""


def set_inputs():
    global N
    N = get_str()
    return


def main():
    setrecursionlimit(100000)
    set_inputs()
    n = int(N)
    ans = 0
    candidates = []
    for i in range(3, len(N)+1):
        candidates.extend(itertools.product([3, 5, 7], repeat=i))
    for c in candidates:
        if 3 in c and 5 in c and 7 in c:
            v = sum(map(lambda x: x[1] * (10 ** x[0]), enumerate(reversed(c))))
            if v <= n:
                ans += 1
    print(ans)
    return


def get_int():
    return int(input())


def get_float():
    return float(input())


def get_str():
    return input().strip()


def get_li():
    return [int(i) for i in input().split()]


def get_lf():
    return [float(f) for f in input().split()]


def get_lc():
    return list(input().strip())


def get_data(n, types):
    if len(types) == 1:
        return [types[0](input()) for _ in range(n)]
    return zip(*(
        [t(x) for t, x in zip(types, input().split())]
        for _ in range(n)
    ))


if __name__ == '__main__':
    main()
