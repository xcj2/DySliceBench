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


def yesno(v, yes="Yes", no="No", upper=False):
    if upper:
        print([yes.upper(), no.upper()][not v])
    else:
        print([yes, no][not v])


def main():
    """エントリーポイント"""
    N = input(int)
    S, T = input(str, str)
    ans = ""
    for n in range(N):
        ans += S[n] + T[n]
    print(ans)


if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
