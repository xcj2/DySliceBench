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
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    maxi, mini = [-1] * N, [INF] * N
    mini[0] = A[0]
    for i in range(1, N):
        mini[i] = min(mini[i - 1], A[i])
    maxi[-1] = A[-1]
    for i in range(N - 2, -1, -1):
        maxi[i] = max(maxi[i + 1], A[i])

    a, b = defaultdict(int), defaultdict(int)
    diff = -1
    for i in range(N):
        d1 = maxi[i] - A[i]
        d2 = A[i] - mini[i]
        diff = max(diff, d1, d2)
        a[d1] += 1
        b[d2] += 1

    print(min(a[diff], b[diff]))


if __name__ == '__main__':
    main()
