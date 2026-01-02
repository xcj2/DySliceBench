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
    A()
    return


# Solve
if __name__ == "__main__":
    A()
