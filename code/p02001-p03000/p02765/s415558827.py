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


def yesno(v):
    print(["Yes", "No"][not v])


# エントリーポイント
def main():
    N, R = input([int, 2])
    print(R if 10 <= N else R + (100 * (10 - N)))


if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
