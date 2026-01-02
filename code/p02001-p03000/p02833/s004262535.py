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
    a = I()
    b = I()
    print(6 - a - b)
    return


# B
def B():
    n = I()
    s, t = input().split(' ')
    ans = []
    for i in range(n):
        ans.append(s[i])
        ans.append(t[i])
    print(''.join(ans))
    return


# C
def C():
    def GCD(a, b):
        if (b == 0):
            return a
        else:
            return GCD(b, a % b)

    a, b = LI()
    print(a * b // GCD(a, b))
    return


# D
def D():
    n = I()
    a = LI()
    cnt = 0
    for i in range(n):
        if a[i] == cnt + 1:
            cnt += 1
    if cnt == 0:
        print(-1)
    else:
        print(n - cnt)
    return


# E
def E():
    n = I()
    if n % 2 != 0:
        print(0)
        return
    ans = 0
    i = 10
    while 1:
        if i > n:
            break
        ans += n // i
        i *= 5
    print(ans)
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
