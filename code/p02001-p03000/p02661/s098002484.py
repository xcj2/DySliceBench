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


def solve():
    n = getN()
    nums = []
    for i in range(n):
        nums.append(getList())

    if n % 2 == 1:
        nums.sort()
        med = nums[(n + 1) // 2 - 1][0]
        nums.sort(key=lambda x: x[1])
        medhigh = nums[(n + 1) // 2 - 1][1]

        print(medhigh - med + 1)
    else:
        nums.sort()
        med = (nums[n // 2 - 1][0] + nums[n // 2][0]) / 2
        nums.sort(key=lambda x: x[1])
        medhigh = (nums[n // 2 - 1][1] + nums[n // 2][1]) / 2
        # print(medhigh, med)
        print(int((medhigh - med) * 2) + 1)


def main():
    # n = getN()
    # for _ in range(n):
    solve()


if __name__ == "__main__":
    solve()