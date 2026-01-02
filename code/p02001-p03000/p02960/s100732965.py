import sys
sys.setrecursionlimit(1000000)
from math import factorial, ceil, floor
from bisect import bisect_right as bsr
from operator import itemgetter as ig
from collections import defaultdict as dd
from collections import deque, Counter as cnt

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
    if not n: return v.copy()
    return [nlist(n[1:], v) for _ in range(n[0])]

class mod:
    def __init__(self, v=0):
        self.v = v
        self.v %= MOD
    def __add__(self, v):
        self.v += v.v
        self.v %= MOD
        return self
    def __str__(self):
        return str(self.v)

# エントリーポイント
def main():
    S = input(str)
    dp = [[mod(0) for _ in range(13)] for _ in range(len(S) + 1)]
    dp[0][0].v = 1
    for i, s in enumerate(S):
        i += 1
        loop = range(10) if s == "?" else [int(s)]
        for n in range(13):
            for m in loop:
                dp[i][(n * 10 + m) % 13] += dp[i - 1][n]
                # dp[i][(n * 10 + m) % 13] %= MOD
    print(dp[-1][5])

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
