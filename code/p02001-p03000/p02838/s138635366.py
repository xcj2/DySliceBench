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

MOD = 10 ** 9 + 7
def solve():
    n = getN()
    bit_array = [[0, 0] for i in range(61)]
    nums = getList()
    for num in nums:
        digit = 0
        while(digit < 61):
            if num % 2 == 0:
                bit_array[digit][0] += 1
            else:
                bit_array[digit][1] += 1
            digit += 1
            num //= 2


    # print(bit_array)
    ans = 0
    for i, tgt in enumerate(bit_array):
        ans += pow(2, i, MOD) * tgt[0] * tgt[1]
        ans %= MOD

    print(ans   )

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    solve()