from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def dfs(i, ws, d, W):
    if i >= len(ws):
        return 0
    w = ws[i]

    ans = dfs(i + 1, ws, d, W)
    total = 0
    for j in range(len(d[w])):
        total += d[w][j]
        if (j + 1) * w <= W:
            ans = max(ans, dfs(i + 1, ws, d, W - (j + 1) * w) + total)
    return ans


def main():
    N, W = map(int, input().split())

    d = defaultdict(list)
    for _ in range(N):
        w, v = map(int, input().split())
        d[w].append(v)
    for w in d.keys():
        d[w].sort(reverse=True)

    print(dfs(0, list(d.keys()), d, W))


if __name__ == '__main__':
    main()
