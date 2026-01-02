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
    s = SI()

    res = 0
    for l in range(len(s)):
        for r in range(l, len(s)):
            t = s[l:r + 1]
            if all([1 if c in 'ACGT' else 0 for c in t]):
                res = max(res, len(t))

    return res


print(main())
