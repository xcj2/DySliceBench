from itertools import permutations as perm
from collections import deque, Counter as cnt
from collections import defaultdict as dd
from operator import itemgetter as ig
from bisect import bisect_right as bsr
from math import factorial, ceil, floor
import sys
sys.setrecursionlimit(1000000)

# お約束
args = None
INF = float("inf")
MOD = int(1e9 + 7)


def input(*ps):
    if type(ps[0]) is list:
        return [input(*ps[0][:-1]) for _ in range(ps[0][-1])]
    elif len(ps) == 1:
        return ps[0](next(args))
    else:
        return [p(next(args)) for p in ps]


def nlist(n, v):
    if not n:
        return [] if type(v) is list else v
    return [nlist(n[1:], v) for _ in range(n[0])]


def yesno(v, yes="Yes", no="No", upper=False):
    if upper:
        print([yes.upper(), no.upper()][not v])
    else:
        print([yes, no][not v])


def is_prime(v):
    if v <= 1:
        return False
    for x in range(2, floor(v ** 0.5)):
        if v % x == 0:
            return False
    return True


def main():
    """エントリーポイント"""
    N = input(int)
    for x in range(N, 100003 + 1):
        if is_prime(x):
            print(x)
            break


if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
