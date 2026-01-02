import sys
import math
import bisect
from collections import defaultdict, deque
from heapq import heappush, heappop


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


def IR(n):
    return [I() for i in range(n)]


# A
def A():
    n = I()
    print(n // 2 - 1 if n % 2 == 0 else n // 2)
    return


# B
def B():
    n = I()
    d = LI()
    if d[0] != 0:
        print(0)
        return
    d.sort()
    if d[1] == 0:
        print(0)
        return
    cnt = []
    prenum = 1
    for i in range(1, max(d) + 1):
        num = bisect.bisect_right(d, i)
        if num - prenum == 0:
            print(0)
            return
        else:
            cnt.append(num - prenum)
            prenum = num
    ans = 1
    for i in range(1, max(d)):
        ans *= cnt[i - 1] ** cnt[i]
    print(ans % 998244353)
    return


# C
def C():
    return


# D
def D():
    return


# E
def E():
    return


# F
def F():
    return


# Unittest
def resolve():
    B()
    return


# Solve
if __name__ == "__main__":
    B()
