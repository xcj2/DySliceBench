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
    n, c, k = LI()
    T = deque(sorted([II() for _ in range(n)]))

    p = T.popleft()
    t = p + k
    res = 0
    while T:
        cnt = 1
        while T and cnt < c and T[0] <= t:
            cnt += 1
            T.popleft()
        res += 1
        p = 0
        if T:
            p = T.popleft()
            t = p + k

    if p:
        res += 1

    return res


print(main())
