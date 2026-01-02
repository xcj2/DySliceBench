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


# 初項s, 交差dのn個の数列の和
def sum_of_arithmetic_progression(s, d, n):
    return n * (2 * s + (n - 1) * d) // 2


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
    N, M = map(int, input().split())
    state = []
    for _ in range(M):
        S = list(map(int, input().split()))

        v = [0] * N
        for s in S[1:]:
            v[s - 1] = 1
        state.append(v)
    P = list(map(int, input().split()))

    ans = 0
    for pattern in product([0, 1], repeat=N):
        all_on = True
        for i in range(M):
            num_on = 0
            for j in range(N):
                if state[i][j] == 1 and pattern[j] == 1:
                    num_on += 1

            if num_on % 2 != P[i]:
                all_on = False
                break

        ans += all_on

    print(ans)

if __name__ == '__main__':
    main()
