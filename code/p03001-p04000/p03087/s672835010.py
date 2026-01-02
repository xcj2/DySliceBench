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

MOD = 998244353
def solve():
    n, q = getList()
    s = input().strip()
    acc = [0]
    tmp = 0
    pred = ""
    for c in s:
        if pred == "A" and c == "C":
            tmp += 1
        acc.append(tmp)
        pred = c

    for i in range(q):
        l, r = getList()
        print(acc[r] - acc[l])

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    solve()