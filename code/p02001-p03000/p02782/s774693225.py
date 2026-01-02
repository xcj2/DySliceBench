import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from  collections import defaultdict
from collections import Counter
import bisect
from functools import reduce

def main():
    mod = 10 ** 9 + 7
    def comb(n, r):
        numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
        denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
        return numerator * pow(denominator, mod - 2, mod) % mod
    r_1, c_1, r_2, c_2 = MI()
    #0<=i<=r, o<=j<=cなる全ての(i,j)についてのf(i,j)の和をg(i,j)とする。これをg_rcと表記する。mはマイナス。
    g_r2c2 = (comb(r_2 + c_2 + 2, c_2 + 1) - 1) % mod
    g_r2c1m1 = (comb(r_2 + c_1 + 1, c_1) - 1) % mod
    g_r1m1c2 = (comb(r_1 + c_2 + 1, c_2 + 1) - 1) % mod
    g_r1m1c1m1 = (comb(r_1 + c_1, c_1) - 1) % mod
    ans = (((((g_r2c2 - g_r2c1m1) % mod) - g_r1m1c2) % mod) + g_r1m1c1m1) % mod

    print(ans)


if __name__ == "__main__":
    main()
