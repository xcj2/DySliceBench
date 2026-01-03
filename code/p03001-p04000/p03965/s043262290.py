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
    S = input()

    ans = 0
    for i, c in enumerate(S):
        if i < ceil(len(S), 2):
            h = "g"
        else:
            h = "p"

        if c == h:
            continue
        elif c == "g" and h == "p":
            ans += 1
        elif c == "p" and h == "g":
            ans -= 1
    print(ans)


if __name__ == '__main__':
    main()
