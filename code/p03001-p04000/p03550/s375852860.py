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


# 相手がi番目を引いたときにだせる最大/最小のスコア
def dfs(turn, i):
    global memo, a
    if memo[turn][i] != -1:
        return memo[turn][i]

    ans = 0 if turn == 0 else INF
    for j in range(i + 1, len(a)):
        if j == len(a) - 1:
            s = abs(a[j] - a[i])
        else:
            s = abs(dfs(1 - turn, j))

        # X
        if turn == 0:
            ans = max(ans, s)
        # Y
        else:
            ans = min(ans, s)

    memo[turn][i] = ans
    return ans


def solve2(N, Z, W):
    global a, memo
    a = [W] + a
    memo = [[-1] * len(a) for _ in range(2)]
    return dfs(0, 0)


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
