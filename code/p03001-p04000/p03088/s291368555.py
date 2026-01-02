import sys
from math import factorial, ceil, floor
from bisect import bisect_right as bsr
from operator import itemgetter as ig
from collections import defaultdict as dd
from collections import deque

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
    if not n: return v
    return [nlist(n[1:], v) for _ in range(n[0])]
import random

# エントリーポイント
def main():
    N = input(int)

    dp = nlist([N + 1, 5, 5, 5], 0)
    dp[0][0][0][0] = 1
    for n in range(1, N + 1):
        for i in range(5):  # ["", "A", "C", "G", "T"]:
            for j in range(5):  # ["", "A", "C", "G", "T"]:
                for k in range(5):  # ["", "A", "C", "G", "T"]:
                    for l in range(1, 5):  # ["A", "C", "G", "T"]:
                        if j == 1 and k == 3 and l == 2: continue
                        if j == 3 and k == 1 and l == 2: continue
                        if j == 1 and k == 2 and l == 3: continue
                        if i == 1 and k == 3 and l == 2: continue
                        if i == 1 and j == 3 and l == 2: continue
                        dp[n][j][k][l] += dp[n - 1][i][j][k]
                        dp[n][j][k][l] %= MOD
    ans = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                ans += dp[N][i][j][k]
                ans %= MOD
    print(ans)

if __name__ == '__main__':
    args = iter(sys.stdin.read().split())
    main()
