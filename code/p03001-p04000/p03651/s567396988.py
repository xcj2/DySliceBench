from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
INF = float("inf")


# aとbの最大公約数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(N, K, A_list):
    A_list = list(sorted(A_list))
    if max(A_list) < K:
        return False

    if K in A_list:
        return True

    x = A_list[0]
    min_d = INF
    for a in A_list:
        min_d = min(min_d, gcd(a, x))

    for a in A_list:
        if a > K and (a - K) % min_d == 0:
            return True
    return False


def main():
    N, K = map(int, input().split())
    A_list = list(map(int, input().split()))

    print("POSSIBLE" if solve(N, K, A_list) else "IMPOSSIBLE")


if __name__ == '__main__':
    main()