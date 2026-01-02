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
    s = S()
    t = S()
    ans = 0
    for i in range(3):
        if s[i] == t[i]:
            ans += 1
    print(ans)
    return


# B
def B():
    a, b = LI()
    print(-(-(b - 1) // (a - 1)))
    return


# C
def C():
    N = I()
    H = LI()
    ans = 0
    cnt = 0
    for i in range(1, N):
        if H[i - 1] >= H[i]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)
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
    C()
    return


# Solve
if __name__ == "__main__":
    C()
