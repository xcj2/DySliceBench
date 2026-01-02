import sys
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache, reduce
from operator import xor
from heapq import heappush, heappop
INF = float("inf")
sys.setrecursionlimit(10**7)

# 4近傍（右, 下, 左, 上）
dy4, dx4 = [0, -1, 0, 1], [1, 0, -1, 0]


def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W
def ceil(a, b):return (a + b - 1) // b


def solve(N, H, a_b):
    max_a = -1
    for a, b in a_b:
        max_a = max(max_a, a)

    good_b = []
    for a, b in a_b:
        if b >= max_a:
            good_b.append(b)

    ans = 0
    for b in sorted(good_b, reverse=True):
        ans += 1
        H -= b
        if H <= 0:
            return ans

    return ans + ceil(H, max_a)


def main():
    N, H = map(int, input().split())
    l = []
    for _ in range(N):
        a, b = map(int, input().split())
        l.append((a, b))
    print(solve(N, H, l))


if __name__ == '__main__':
    main()
