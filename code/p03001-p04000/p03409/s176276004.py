# coding:utf-8

import sys
import random
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    red = [LI() for _ in range(n)]
    blue = [LI() for _ in range(n)]
    blue.sort()

    used = [0] * n
    res = 0
    for a, b in blue:
        t = -1
        k = -1
        for i, (x, y) in enumerate(red):
            if used[i]:
                continue

            if x < a and b > y > t:
                t = y
                k = i

        if k != -1:
            used[k] = 1
            res += 1

    return res


print(main())
