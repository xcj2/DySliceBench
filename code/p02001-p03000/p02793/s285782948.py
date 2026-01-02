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
    N = int(readline())
    A = list(map(int, readline().split()))

    lcmnum = 1
    def gcd(a, b):
        if (a == 0):
            return b
        return gcd(b%a, a)

    def lcm(x, y):
        return (x * y) // gcd(x, y)
    for a in A:
        lcmnum = lcm(lcmnum, a)

    ans = 0
    for a in A:
        a = lcmnum // a
        ans += a
    ans %= mod

    print(ans)




if __name__ == '__main__':
    solve()
