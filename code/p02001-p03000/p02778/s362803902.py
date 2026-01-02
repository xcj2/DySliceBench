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
    s, t = input().split()
    a, b = LI()
    u = input()
    if u == s:
        print("{} {}".format(a - 1, b))
    elif u == t:
        print("{} {}".format(a, b - 1))
    return


# B
def B():
    s = input()
    print('x' * len(s))
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


# Solve
if __name__ == "__main__":
    B()
