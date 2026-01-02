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


def main():
    n, k = LI()
    s = '0' + SI() + '0'

    L = []
    R = []
    if s[1] == '0':
        L.append(1)
        R.append(1)
    for i in range(n + 1):
        if s[i] == '1' and s[i + 1] == '0':
            R.append(i)
        if s[i] == '0' and s[i + 1] == '1':
            L.append(i + 1)

    if s[-2] == '0':
        L.append(n)
        R.append(n)

    res = R[0] - L[0] + 1
    k = min(len(R) - 1, k)
    for i in range(len(R) - k):
        res = max(res, R[i + k] - L[i] + 1)

    # print(R)
    # print(L)

    return res


print(main())
