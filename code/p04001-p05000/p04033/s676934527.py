# coding:utf-8

import sys
from collections import defaultdict, deque

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    a, b = LI()

    if a <= 0 and b >= 0:
        return 'Zero'

    if a > 0:
        return 'Positive'

    if (b - a) % 2:
        return 'Positive'
    else:
        return 'Negative'


print(main())
