# coding:utf-8

import sys
import fractions

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        x, y = y, x % y
        return gcd(x, y)


def main():
    n = II()
    A = LI()
    A.sort()
    A.reverse()

    pre = [0] * n
    pre[0] = A[0]
    for i in range(1, n):
        pre[i] = gcd(pre[i - 1], A[i])
    res = pre[-1]
    for i in range(n):
        t = pre[i]
        for j in range(i + 2, n):
            t = gcd(t, A[j])
            if t == pre[j - 1]:
                t = -1
                break
        res = max(res, t)

    t = A[1]
    for a in A[1:]:
        t = gcd(t, a)

    return max(res, t)


print(main())
