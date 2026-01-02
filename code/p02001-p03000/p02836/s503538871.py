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
    a, b, c = LI()
    if a + b + c >= 22:
        print("bust")
    else:
        print("win")
    return


# B
def B():
    s = S()
    ans = 0
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            ans += 1
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
