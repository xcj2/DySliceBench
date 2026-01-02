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
    r, g, b, n = LI()

    res = 0
    for ri in range(n // r + 1):
        for gi in range(n // g + 1):
            t = n - r * ri - g * gi
            if t >= 0 and t % b == 0:
                res += 1

    print(res)


if __name__ == '__main__':
    main()
