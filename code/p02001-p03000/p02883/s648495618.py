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
    a, b, x = LI()
    if (x <= a * a * b / 2):
        print(math.degrees(math.atan(a * b * b / x / 2)))
    else:
        print(math.degrees(math.atan(2 * (a * a * b - x) / a ** 3)))
    return


# E
def E():
    n, k = LI()
    a = LI()
    f = LI()
    a.sort()
    f.sort(reverse=True)
    left = 0
    right = 0
    for a_i, f_i in zip(a, f):
        right = max(a_i * f_i, right)
    while (left != right):
        mid = (left + right) >> 1
        score = 0
        for i in range(n):
            if a[i] * f[i] > mid:
                score += a[i] - mid // f[i]
        if score <= k:
            right = mid
        else:
            left = mid + 1
    print(left)
    return


# F
def F():
    return


# Unittest
def resolve():
    E()
    return


# Solve
if __name__ == "__main__":
    E()
