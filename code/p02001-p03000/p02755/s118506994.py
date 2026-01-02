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
    S = input()
    if S == 'AAA' or S == 'BBB':
        print('No')
    else:
        print('Yes')
    return


# B
def B():
    N, A, B = LI()
    ans = N // (A + B) * A + min(N % (A + B), A)
    print(ans)
    return


# C
def C():
    A, B = LI()
    for i in range(1, 1001):
        if i * 8 // 100 == A and i * 10 // 100 == B:
            print(i)
            return
    print(-1)
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
    C()
