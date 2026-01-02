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

def yaku(n):
    res = []
    for i in range(2, int(math.sqrt(n)) + 2):
        tmp = 0
        while(True):
            if n % i == 0:
                tmp += 1
                n //= i
            else:
                break
        if tmp != 0:
            res.append((tmp, i))
    if n != 1:
        res.append((1, n))
    return res

def solve():
    n = getN()
    acc = [0]
    tmp = 0
    for i in range(1, 10**6):
        tmp += i
        acc.append(tmp)

    res = yaku(n)
    ans = 0
    for y in res:
        ans += bisect_right(acc, y[0]) - 1
    # print(res)
    print(ans)

def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    solve()