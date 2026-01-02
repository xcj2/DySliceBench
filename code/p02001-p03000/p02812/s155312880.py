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
    K, X = LI()
    if K * 500 >= X:
        print("Yes")
    else:
        print("No")
    return


# B
def B():
    n = I()
    s = S()
    cnt = 0
    for i in range(n - 2):
        if s[i] == "A":
            if s[i + 1] == "B"  and s[i + 2] == "C":
                cnt += 1
    print(cnt)
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
