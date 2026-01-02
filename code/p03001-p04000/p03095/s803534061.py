# coding:utf-8

import sys
from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    s = SI()

    cnt = [0] * 27
    res = 0
    for c in s:
        k = ord(c) - 97
        cnt[k] += 1
        tmp = 1
        for i in range(27):
            if not cnt[i]:
                continue
            if i == k:
                continue
            tmp *= cnt[i] + 1
        res += tmp
        res %= MOD

    return res if res else MOD


print(main())
