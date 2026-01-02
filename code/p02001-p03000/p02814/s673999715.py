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
            if s[i + 1] == "B" and s[i + 2] == "C":
                cnt += 1
    print(cnt)
    return


# C
def C():
    n = I()
    p = LI()
    q = LI()
    a_cnt = [1] * n
    b_cnt = [1] * n
    a = 0
    b = 0
    for i in range(1, n + 1):
        num = 1
        for j in range(1, n + 1 - i):
            num *= j
        a += sum(a_cnt[:p[i - 1]]) * num
        b += sum(b_cnt[:q[i - 1]]) * num
        a_cnt[p[i - 1] - 1] = 0
        b_cnt[q[i - 1] - 1] = 0
    print(abs(a - b))
    return


# D
def D():
    def GCD(a, b):
        if (b == 0):
            return a
        else:
            return GCD(b, a % b)

    n, m = LI()
    a = list(int(x) // 2 for x in sys.stdin.readline().split())
    b = a[0]
    for i in range(1, n):
        b = b * a[i] // GCD(b, a[i])
        if (b // a[i]) % 2 == 0:
            print(0)
            return
    if b > m:
        print(0)
    else:
        print((m - b) // (b * 2) + 1)
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
