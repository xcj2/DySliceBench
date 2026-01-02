import sys
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

def nck(n, k, kaijyo):
    if n < k:
        return 0
    if n == k:
        return 1
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD

def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return 1
    return (kaijyo[n] * divide(kaijyo[n-k])) % MOD

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
    n, k = getList()
    nums = getList()
    nums.sort()
    kai, _ = fact_and_inv(n+2)
    # print(kai)
    # print(kai)
    # print(npk(5,5,kai))
    # print(nck(5,4,kai))
    # for nn in nums:
    #     print(nn)
    # print(MOD)
    mn, mx = 0, 0
    for i in range(n-k+1):
        # print(n-i-1, k-1)
        pat = nck(n-i-1, k-1, kai)
        mn += pat * nums[i]
        mx += pat * nums[-i-1]

        mn %= MOD
        mx %= MOD
        # print(mx, mn)
    print((mx - mn + MOD) % MOD)


def main():
    n = getN()
    for _ in range(n):
        solve()

    return
if __name__ == "__main__":
    # main()
    solve()





