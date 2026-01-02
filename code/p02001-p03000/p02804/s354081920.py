import sys
import bisect
import itertools
import collections
import fractions
import heapq
import math
from operator import mul
from functools import reduce
from functools import lru_cache


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    N, K = map(int, readline().split())
    A = list(map(int, readline().split()))

    A.sort()
    lenA = len(A)
    ans = 0

    if K == 1:
        print(0)
        sys.exit()

    def com(n, r, mod):
        r = min(r, n - r)
        if r == 0:
            return 1
        res = ilist[n] * iinvlist[n - r] * iinvlist[r] % mod
        return res

    def modinv(a, mod=10 ** 9 + 7):
        return pow(a, mod - 2, mod)

    ilist = [0]
    iinvlist = [1]
    tmp = 1
    for i in range(1, N + 1):
        tmp *= i
        tmp %= mod
        ilist.append(tmp)
        iinvlist.append(modinv(tmp, mod))

    sum_of_com = []
    now = 0

    for i in range(K-2, N+1):
        now += com(i, K-2, mod)
        sum_of_com.append(now)

    ans = 0
    for first in range(lenA-K+1):
        ans -= A[first] * sum_of_com[lenA-first-K]
    for last in range(K-1, lenA):
        ans += A[last] * sum_of_com[last-K+1]
    ans %= mod
    print(ans)

if __name__ == '__main__':
    solve()