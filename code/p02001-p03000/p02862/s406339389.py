import sys
import math
import bisect
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from operator import mul
from functools import reduce


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def I(): return int(sys.stdin.readline())


def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res


# A
def A():
    r = I()
    print(r * r)
    return


# B
def B():
    N = I()
    s = S()
    if N % 2 != 0:
        print("No")
    elif ''.join(s[:N // 2]) == ''.join(s[N // 2:]):
        print("Yes")
    else:
        print("No")
    return


# C
def C():
    n = I()
    a = [LI() for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += pow(pow(a[i][0] - a[j][0], 2) + pow(a[i][1] - a[j][1], 2), 0.5)
    avg = ans / (n * (n - 1) / 2)
    print(avg * (n - 1))
    return


# D
def D():
    X, Y = LI()

    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod

    mod = 10 ** 9 + 7  # 出力の制限
    N = X + Y
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル

    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    if (X + Y) % 3 != 0:
        print(0)
    elif X < ((X + Y) // 3) or Y < ((X + Y) // 3):
        print(0)
    else:
        print(cmb((X + Y) // 3, min(X, Y) - ((X + Y) // 3), mod))

    return


# E
def E():
    return


# F
def F():
    return


# Unittest
def resolve():
    D()
    return


# Solve
if __name__ == "__main__":
    D()
