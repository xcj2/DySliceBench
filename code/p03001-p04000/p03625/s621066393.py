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
    N = int(input())
    C = Counter(list(map(int, input().split())))

    s1 = list(sorted([k for k, v in C.items() if v >= 2], reverse=True))
    s2 = list(sorted([k for k, v in C.items() if v >= 4], reverse=True))

    ans = 0
    if len(s1) >= 2:
        ans = max(ans, s1[0] * s1[1])
    if len(s2) >= 1:
        ans = max(ans, s2[0] ** 2)
    print(ans)


if __name__ == '__main__':
    main()
