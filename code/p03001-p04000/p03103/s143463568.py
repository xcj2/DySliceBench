# coding:utf-8

import sys
from collections import deque, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n, m = LI()
    AB = [LI() for _ in range(n)]
    AB.sort()
    AB = deque(AB)

    cnt = 0
    res = 0
    while cnt < m:
        a, b = AB.popleft()
        cnt += b
        res += a * b

    if cnt > m:
        res -= a * (cnt - m)

    return res


print(main())
