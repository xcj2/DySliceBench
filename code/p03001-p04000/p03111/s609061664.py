# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, a, b, c = LI()
A = [a, b, c]
K = [II() for _ in range(n)]


def DFS(cur, x, y, z):
    if cur == n:
        return abs(x - a) + abs(y - b) + abs(z - c) - 30 if min(x, y, z) > 0 else INF
    ret0 = DFS(cur + 1, x, y, z)
    ret1 = DFS(cur + 1, x + K[cur], y, z) + 10
    ret2 = DFS(cur + 1, x, y + K[cur], z) + 10
    ret3 = DFS(cur + 1, x, y, z + K[cur]) + 10
    return min(ret0, ret1, ret2, ret3)


print(DFS(0, 0, 0, 0))
