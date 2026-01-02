# coding:utf-8

import sys
import math
INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    a, b = LS()

    is_square = False
    n = int(a + b)
    t = 1
    while t ** 2 <= n:
        if t ** 2 == n:
            is_square = True
        t += 1

    return 'Yes' if is_square else 'No'


print(main())
