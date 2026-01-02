from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
INF = float("inf")
import sys
sys.setrecursionlimit(10000)

a = []
memo = []


def dfs(no, i):
    global memo, a
    if memo[no][i] != -1:
        return memo[no][i]

    ans = abs(a[-1] - a[i])
    for j in range(i + 1, len(a) - 1):
        nex = dfs(1 - no, j + 1)
        # X
        if no == 0:
            ans = max(ans, nex)
        # Y
        else:
            ans = min(ans, nex)

    memo[no][i] = ans
    return ans


def solve2(N, Z, W):
    global a, memo
    a = [Z, W] + a
    memo = [[-1] * len(a) for _ in range(2)]
    return dfs(0, 1)


def solve(N, Z, W):
    global a
    ans = abs(a[-1] - W)
    if len(a) > 1:
        ans = max(ans, abs(a[-2] - a[-1]))
    return ans


def main():
    global a
    N, Z, W = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve2(N, Z, W))


if __name__ == '__main__':
    main()
