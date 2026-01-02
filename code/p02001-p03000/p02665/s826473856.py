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
    return 1/f


def combmod(n, k, mod=MOD):
    ret = 1
    for i in range(n - k + 1, n + 1):
        ret *= i
        ret %= mod

    for i in range(1, k + 1):
        ret *= pow(i, mod - 2, mod)
        ret %= mod

    return ret

def solve():
    n = getN()
    nums = getList()
    # 1段しかない
    if n == 0:
        if nums[0] == 1:
            print(1)
        else:
            print(-1)
        return
    # 1段目で終わり(かなしいね)
    if nums[0] > 0:
        print(-1)
        return

    acc = []
    tmp = 0
    for i , num in enumerate(nums[::-1]):
        tmp += num
        acc.append(tmp)
    acc.reverse()

    ans = 1
    ue = 1
    for i, num in enumerate(nums[1:-1]):
        if ue * 2 <= num:
            print(-1)
            return
        konodan = min(ue * 2, acc[i+1])
        # print(konodan)
        ans += konodan
        ue = konodan - num

    if ue * 2 < nums[-1]:
        print(-1)
        return

    print(ans + nums[-1])
    return


def main():
    # n = getN()
    # for _ in range(n):
    solve()
if __name__ == "__main__":
    solve()

"""
    12
    3 2
    3 2
    0 1
    2 -1
    -3 -9
    -8 12
    7 0
    8 1
    8 2
    8 4
    0 0
    0 0
"""