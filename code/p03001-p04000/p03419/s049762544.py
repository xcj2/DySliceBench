# coding:utf-8

import sys
from collections import deque

INF = float('inf')
MOD = 10 ** 9 + 7
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n, m = LI()

    if max(n, m) == 1:
        print(1)
    elif n == 1:
        print(max(0, m - 2))
    elif m == 1:
        print(max(0, n - 2))
    elif n == 2 or m == 2:
        print(0)
    else:
        print((n - 2) * (m - 2))


if __name__ == '__main__':
    main()
