#from math import sqrt
#from heapq import heappush, heappop
#from collections import deque
from functools import reduce

#a, b = [int(v) for v in input().split()]


def main():

    n, a, b = map(int, input().split())
    mod = 1000000007

    def pow(n, r):
        if r == 0:
            return 1
        val = pow(n, r // 2)
        val = val * val % mod
        if r % 2 == 1:
            val = val * n % mod
        return val

    def comb(n, r):
        over = 1
        under = 1
        for i in range(r):
            over = over * (n - i) % mod
            under = under * (i + 1) % mod

        return over * pow(under, mod - 2) % mod

    ans = pow(2, n) - 1 - comb(n, a) - comb(n, b) % mod
    while ans < 0:
        ans += mod
    print(ans)


main()
