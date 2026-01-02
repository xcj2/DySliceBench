import sys
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
    return


# B
def B():
    return


# C
def C():
    n = I()
    for i in range(int(n ** 0.5), 0, -1):
        if n % i == 0:
            print(i + n // i - 2)
            return
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