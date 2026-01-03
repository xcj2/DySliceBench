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
    n = int(input())
    d = defaultdict(int)
    for c in ascii_lowercase:
        d[c] = 100

    for _ in range(n):
        count = Counter(input())
        for c in ascii_lowercase:
            d[c] = min(d[c], count[c])

    ans = ""
    for k, v in sorted(d.items()):
        if v > 0:
            ans += k * v

    print(ans)


if __name__ == '__main__':
    main()
