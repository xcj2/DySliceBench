def getN():
    return int(input())


def getNM():
    return map(int, input().split())


def getList():
    return list(map(int, input().split()))


from collections import defaultdict, deque, Counter
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
    MOD = 2019
    s = input().strip()
    acc = [0]
    revgen = pow(10, MOD-2, MOD)
    for c in s:
        num = int(c)
        acc.append((acc[-1] * 10 + num) % MOD)

    acc.reverse()
    mul = 1
    res = []
    for ac in acc:
        ac *= mul
        ac %= MOD
        res.append(ac)
        mul *= 10
        mul %= MOD
    res.reverse()

    # print(res)
    cnt = Counter(res)
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1)
    print(ans // 2)
    # print(acc)
    # print((1817 * 100000) % MOD)
    # print((817 * 100000) % MOD)
def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    solve()