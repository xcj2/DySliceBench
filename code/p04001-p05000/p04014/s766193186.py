from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, floor
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


def f(b, n):
    if n < b:
        return n
    return f(b, n // b) + n % b


def main():
    N = int(input())
    S = int(input())

    if N == S:
        print(N + 1)
        return
    if N < S:
        print(-1)
        return

    ans = INF
    for b in range(2, int(sqrt(N)) + 1):
        if f(b, N) == S:
            ans = min(ans, b)

    bs = set()
    t = N - S
    for i in range(1, int(sqrt(N)) + 1):
        if t % i == 0:
            bs.add(i + 1)
            bs.add((t // i) + 1)
    
    for b in bs:
        if b == 1:
            continue
        if f(b, N) == S:
            ans = min(ans, b)

    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
