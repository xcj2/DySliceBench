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
    N, A, B = MI()
    p = pow(2, N, mod) - 1
    a = comb(N, A)
    b = comb(N, B)
    ans = (p - a - b) % mod
    print(ans)


if __name__ == "__main__":
    main()
