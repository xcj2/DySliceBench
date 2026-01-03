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

ans = 0
def dfs(i, S, l):
    global ans
    if i >= len(S) - 1:
        pre = 0
        for j in l + [len(S) - 1]:
            ans += int(S[pre:j + 1])
            pre = j + 1
        return

    dfs(i + 1, S, l[:] + [i])
    dfs(i + 1, S, l[:])


def main():
    S = input()
    dfs(0, S, [])
    print(ans)


if __name__ == '__main__':
    main()
