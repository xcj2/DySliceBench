# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


# 整数(x, y)最大公約数を求める
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        x, y = y, x % y
        return gcd(x, y)


n = II()
A = LI()

ans = A[0]
for a in A:
    ans = gcd(ans, a)

print(ans)
