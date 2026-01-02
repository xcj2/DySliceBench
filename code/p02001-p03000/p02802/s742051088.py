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


def main():
    """エントリーポイント"""
    N, M = input([int, 2])
    PS = input([[str, 2], M])

    ans = {}
    for p, s in PS:
        if not p in ans:
            ans[p] = [0, 0]
        if s == "AC":
            ans[p][0] = 1
        if s == "WA" and ans[p][0] == 0:
            ans[p][1] += 1
    ac, pen = 0, 0
    for v in ans.values():
        if v[0] == 0:
            continue
        ac += 1
        pen += v[1]
    print(ac, pen)


if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
