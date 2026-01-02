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


def main():
    H, W = map(int, input().split())
    f = []
    for _ in range(H):
        f.append(input())

    ans = [[0] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if f[y][x] == "#":
                ans[y][x] = "#"
                continue
            num = 0
            for i in range(8):
                ny, nx = dy8[i] + y, dx8[i] + x
                if inside(ny, nx, H, W) and f[ny][nx] == "#":
                    num += 1

            ans[y][x] = num

    for line in ans:
        print(*line, sep="")


if __name__ == '__main__':
    main()
