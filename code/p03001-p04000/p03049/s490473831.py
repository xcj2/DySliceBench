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

    ans = 0
    a, b, ba = 0, 0, 0
    for _ in range(N):
        S = input()
        ans += S.count("AB")

        if S[0] == "B" and S[-1] == "A":
            ba += 1
        elif S[-1] == "A":
            a += 1
        elif S[0] == "B":
            b += 1

    # A B A B
    if a > 0 and ba:
        a -= 1
        ans += ba

        if b > 0:
            ans += 1
            b -= 1
    elif a == 0 and ba:
        ans += ba - 1
        if b > 0:
            ans += 1
            b -= 1

    # A B
    ans += min(a, b)

    print(ans)


if __name__ == '__main__':
    main()
