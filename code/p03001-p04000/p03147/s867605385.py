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


# aとbの最大公約数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# aとbの最小公倍数
def lcm(a, b):
    g = gcd(a, b)
    return a / g * b


def main():
    N = int(input())
    H = list(map(int, input().split())) + [0]

    ans = 0
    change = True
    while change:
        change = False

        left = 0
        found = False
        for i in range(len(H)):
            if H[i] != 0:
                if not found:
                    found = True
                    left = i

            if H[i] == 0:
                if found:
                    ans += 1
                    change = True
                    for j in range(left, i):
                        H[j] -= 1

                    left = i + 1
                    found = False

    print(ans)


if __name__ == '__main__':
    main()
