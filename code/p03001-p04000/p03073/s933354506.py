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

    r, t = 0, 0
    for i in range(len(s)):
        if i % 2:
            if s[i] == '0':
                r += 1
            else:
                t += 1
        else:
            if s[i] == '0':
                t += 1
            else:
                r += 1

    return min(r, t)


print(main())
