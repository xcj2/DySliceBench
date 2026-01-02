import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
import bisect
from functools import reduce
def main():
    def comb(n, r):
        numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
        denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
        return numerator * pow(denominator, mod - 2, mod) % mod
    mod = 10 ** 9 + 7
    N, K = MI()
    if K >= N - 1:
        ans = comb(2 * N - 1, N - 1)
        print(ans)
    else:
        N_r = pow(N, mod - 2, mod)
        ans = N * (N - 1) % mod
        add = N * (N - 1) % mod
        for i in range(2, K + 1):
            a = (N - i + 1) % mod
            b = (a - 1) % mod
            c = pow(i, mod - 2, mod)
            d = pow(c, 2, mod)
            add = ((((add * a) % mod * b) % mod) * d) % mod
            ans += add
            ans %= mod
        if K >= 2:
            ans += 1
            ans %= mod
        print(ans)

if __name__ == "__main__":
    main()