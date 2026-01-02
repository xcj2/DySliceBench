from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
INF = float("inf")
import sys
sys.setrecursionlimit(10000)


# 初項a，交差dの数列n個の和
def arithmetic_series(a, d, n):
    return n * (2 * a + (n - 1) * d) // 2


def solve(A):
    ans = arithmetic_series(1, 1, len(A) - 1) + 1
    c = Counter(A)
    for v in c.values():
        ans -= (v * (v - 1)) // 2
    return ans


def main():
    A = input()
    print(solve(A))


if __name__ == '__main__':
    main()
