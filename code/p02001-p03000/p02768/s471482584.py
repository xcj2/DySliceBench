# from math import sqrt
# from heapq import heappush, heappop
# from collections import deque
from operator import mul
from functools import reduce
# a, b = [int(v) for v in input().split()]


def main():

    mod = 1000000007
    n, a, b = map(int, input().split())

    def combi(n, r):
        if r < 0 or r > n:
            return 0
        r = min(n - r, r)

        over = 1
        under = 1

        for i in range(n - r + 1, n + 1):
            over = over * i % mod

        for i in range(1, r + 1):
            under = under * i % mod

        return over * modpow(under, mod-2) % mod

    def modpow(n, r):
        if r == 0:
            return 1

        v = modpow(n, r // 2)
        v = v * v % mod
        if r % 2 != 0:
            v = v * n % mod
        return v

    ans = modpow(2, n) - 1
    ans -= combi(n, a)
    ans -= combi(n, b)

    while ans < 0:
        ans += mod

    print(ans)


main()
