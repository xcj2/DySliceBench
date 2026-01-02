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
    x, y = map(int, readline().split())
    ans = 0
    tmp = 1

    def modinv(a, mod=10 ** 9 + 7):
        return pow(a, mod - 2, mod)

    def com(n, r, mod):
        r = min(r, n - r)
        if r == 0:
            return 1
        res = ilist[n] * iinvlist[n - r] * iinvlist[r] % mod
        return res

    ilist = [0]
    iinvlist = [1]
    tmp = 1


    for i in range(1, x + y + 1):
        tmp *= i
        tmp %= mod
        ilist.append(tmp)
        iinvlist.append(modinv(tmp, mod))


    for b in range(x//2+1):
        a = x - 2 * b
        if 2*a + b == y:
            ans += ilist[a+b] * iinvlist[a] * iinvlist[b] % mod
    print(ans)


if __name__ == '__main__':
    solve()