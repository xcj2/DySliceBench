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

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def solve():
    n, m = getList()
    st = []
    for i in range(n):
        st.append(getList())

    ch = []
    for i in range(m):
        ch.append(getList())

    for s in st:
        tmp = 10 ** 9
        ans = -1
        for idx, c in enumerate(ch):
            if dist(s, c) < tmp:
                ans = idx + 1
                tmp = dist(s,c)

        print(ans)


def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    solve()