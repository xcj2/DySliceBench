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
    n, m = LI()
    if n == m:
        print("Yes")
    else:
        print("No")

    return


# B
def B():
    a, b = LI()
    if a <= b:
        ans = str(a) * b
    else:
        ans = str(b) * a
    print(ans)
    return


# C
def C():
    n = I()
    p = LI()
    n_min = n + 1
    ans = 0
    for num in p:
        if num < n_min:
            ans += 1
            n_min = num
    print(ans)
    return


# D
def D():
    n = I()
    cnt = [[0] * 10 for i in range(10)]
    ans = 0
    for i in range(1, n + 1):
        h = str(i)[0]
        t = str(i)[-1]
        cnt[int(h)][int(t)] += 1
    for i in range(1, 10):
        for j in range(1, 10):
            ans += cnt[i][j] * cnt[j][i]
    print(ans)
    return


# E
def E():
    return


# F
def F():
    return


# Solve
if __name__ == "__main__":
    D()
