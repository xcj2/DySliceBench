def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))


from collections import defaultdict, deque
from sys import exit
import math
import copy
from bisect import bisect_left, bisect_right
from heapq import *
import sys

# sys.setrecursionlimit(1000000)
INF = 10 ** 17
MOD = 1000000007

from fractions import *


def inverse(f):
    # return Fraction(f.denominator,f.numerator)
    return 1 / f


def combmod(n, k, mod=MOD):
    ret = 1
    for i in range(n - k + 1, n + 1):
        ret *= i
        ret %= mod

    for i in range(1, k + 1):
        ret *= pow(i, mod - 2, mod)
        ret %= mod

    return ret


def bunsu(n):
    ret = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            tmp = 0
            while (True):
                if n % i == 0:
                    tmp += 1
                    n //= i
                else:
                    break
            ret.append((i, tmp))

    ret.append((n, 1))
    return ret

MOD = 998244353
def solve():
    n, k = getList()
    nums = getList()
    dp = [0 for i in range(k+1)]
    dp[0] = 1
    for i, num in enumerate(nums):
        new = [0 for i in range(k+1)]
        for j, d in enumerate(dp):
            new[j] += d * 2
            if (j + num) <= k:
                new[j+num] += d

        dp = [ne%MOD for ne in new]
    print(dp[-1])

def main():
    # n = getN()
    # for _ in range(n):
    solve()


if __name__ == "__main__":
    solve()