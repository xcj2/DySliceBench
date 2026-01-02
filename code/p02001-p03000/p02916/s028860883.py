import sys
import math
import bisect
from collections import defaultdict, deque, Counter
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
    N = I()
    print(pow(N, 3))
    return


# B
def B():
    N = I()
    A = LI()
    B = LI()
    C = LI()
    a_p = -1
    ans = 0
    for a in A:
        if (a - a_p == 1):
            ans += B[a - 1] + C[a - 2]
        else:
            ans += B[a - 1]
        a_p = a
    print(ans)
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
