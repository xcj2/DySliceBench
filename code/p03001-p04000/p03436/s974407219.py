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


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def solve():
    H, W = map(int, input().split())

    num_white = 0
    field = []
    for _ in range(H):
        field.append(list(input()))
        num_white += field[-1].count(".")

    memo = [[INF] * W for _ in range(H)]
    memo[0][0] = 1

    que = deque()
    que.append((0, 0))
    while que:
        y, x = que.popleft()
        c = memo[y][x]

        for i in range(len(dy4)):
            ny, nx = y + dy4[i], x + dx4[i]

            if inside(ny, nx, H, W) and memo[ny][nx] > c + 1 and field[ny][nx] == '.':
                memo[ny][nx] = c + 1
                que.append((ny, nx))

    if memo[-1][-1] == INF:
        return -1
    else:
        return num_white - memo[H - 1][W - 1]


def main():
    print(solve())


if __name__ == '__main__':
    main()
