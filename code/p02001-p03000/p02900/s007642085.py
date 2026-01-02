from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt


def LI(): return list(map(int, input().split()))


def LF(): return list(map(float, input().split()))


def LI_(): return list(map(lambda x: int(x)-1, input().split()))


def II(): return int(input())


def IF(): return float(input())


def LS(): return list(map(list, input().split()))


def S(): return list(input().rstrip())


def IR(n): return [II() for _ in range(n)]


def LIR(n): return [LI() for _ in range(n)]


def FR(n): return [IF() for _ in range(n)]


def LFR(n): return [LI() for _ in range(n)]


def LIR_(n): return [LI_() for _ in range(n)]


def SR(n): return [S() for _ in range(n)]


def LSR(n): return [LS() for _ in range(n)]


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def gcdx(x, y):
    g = 0
    if (x % y != 0):
        g = x % y
        gcdx(y, g)
    return g


mod = 1000000007
inf = float('INF')


def A():
    a = II()
    b = a//2
    p = b/a
    if a % 2:
        print(1-p)
    else:
        print(p)

    return

# B


def B():
    N, K = map(int, input().split())
    h = LI()
    count = 0

    for i in h:
        if i >= K:
            count += 1
        else:
            continue
    print(count)
    return

# C


def C():
    N = II()
    A = LI()
    J = [0] * N
    for i, n in enumerate(A):
        J[n-1] = i+1
    for s in J:
        print(s, end=" ")

    return

# D


def D():
    A, B = map(int, input().split())
    g = gcd(A, B)
    go = g
    myset = set([1])
    sq = int(sqrt(g)) + 2

    for i in range(2, sq):
        while g % i == 0:
            g /= i
            myset.add(i)
        if g == 1:
            break
        if i == sq - 1:
            myset.add(go)

    print(len(myset))

    return

# E


def E():
    N, M = LI()

    price = [-1] * N

    for i in range(M):
        a, b = LI()
        c = LI()
        for k in c:
            if price[k-1] > a or price[k-1] == -1:
                price[k-1] = a
    print(sum(price))

    return

# F


def F():
    return


# Solve
if __name__ == '__main__':
    D()
