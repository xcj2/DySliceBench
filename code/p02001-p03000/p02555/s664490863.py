import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
from collections import deque
import bisect
from decimal import *
from functools import reduce
def main():
    def comb(n, r):
        if r == 0:
            return 1
        else:
            numerator = reduce(lambda x, y: x * y % mod, [n - r + k + 1 for k in range(r)])
            denominator = reduce(lambda x, y: x * y % mod, [k + 1 for k in range(r)])
            return numerator * pow(denominator, mod - 2, mod) % mod
    S = I()
    mod = 10 ** 9 + 7
    N = S // 3
    ans = 0
    for i in range(1, N + 1):
        x = S - 3 * i
        ans += comb(x + i - 1, i - 1)
        ans %= mod
    print(ans)
if __name__ == "__main__":
    main()

