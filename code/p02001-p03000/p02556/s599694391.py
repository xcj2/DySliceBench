import sys
import re
import random
import math
import copy
from heapq import heappush, heappop, heapify
from functools import cmp_to_key
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline
getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = float("inf")
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def fact_and_inv(SIZE):
    inv = [0] * SIZE  # inv[j] = j^{-1} mod MOD
    fac = [0] * SIZE  # fac[j] = j! mod MOD
    finv = [0] * SIZE  # finv[j] = (j!)^{-1} mod MOD
    inv[1] = 1
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    for i in range(2, SIZE):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        fac[i] = fac[i - 1] * i % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    return fac, finv

def solve():
    n = getN()

    points = [getList() for i in range(n)]

    inf = 10 ** 10

    org = []
    far = []
    for x, y in points:
        org.append(x + y)
        far.append(y + inf-x)

    org.sort()
    far.sort()

    a1 = abs(org[0] - org[-1])
    a2 = abs(far[0] - far[-1])

    ans = max(a1, a2)
    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()