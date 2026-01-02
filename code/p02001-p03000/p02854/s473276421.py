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
    X, Y = LI()
    ans = 0
    if X == 1:
        ans += 300000
    elif X == 2:
        ans += 200000
    elif X == 3:
        ans += 100000

    if Y == 1:
        ans += 300000
    elif Y == 2:
        ans += 200000
    elif Y == 3:
        ans += 100000

    if X == 1 and Y == 1:
        ans += 400000

    print(ans)
    return


# B
def B():
    N = I()
    A = LI()
    A_sum = sum(A)
    cnt = 0
    ans = sum(A)
    for i in range(N):
        cnt += A[i]
        sa = abs(A_sum - cnt - cnt)
        ans = min(ans, sa)
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
