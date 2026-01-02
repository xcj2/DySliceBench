import sys
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, ceil, floor
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
def ceil(a, b): return (a + b - 1) // b


def main():
    N = int(input())
    a = Counter(list(map(int, input().split())))

    ans = 0
    for k, v in a.items():
        if k == v:
            continue
        elif k < v:
            ans += v - k
        else:
            ans += v
    print(ans)

if __name__ == '__main__':
    main()
