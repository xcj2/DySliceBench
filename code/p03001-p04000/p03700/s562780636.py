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


def ok(n, A, B, H):
    num = 0
    for h in H:
        r = h - n * B
        if r > 0:
            num += ceil(r, (A - B))
    return num <= n


def main():
    N, A, B = map(int, input().split())
    H = sorted([int(input()) for _ in range(N)])

    low, high = 0, 10 ** 10
    ans = 0
    while high - low > 1:
        middle = (low + high) // 2
        if ok(middle, A, B, H):
            ans = middle
            high = middle
        else:
            low = middle

    print(ans)


if __name__ == '__main__':
    main()
