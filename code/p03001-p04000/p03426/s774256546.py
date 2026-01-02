# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


h, w, d = LI()
coord = [0] * (h * w)
for y in range(h):
    for x, n in enumerate(LI_()):
        coord[n] = (y, x)

C = [[0] for _ in range(d)]
for i in range(d, h * w):
    diff = abs(coord[i][0] - coord[i - d][0]) + abs(coord[i][1] - coord[i - d][1])
    C[i % d].append(C[i % d][-1] + diff)

q = II()
for _ in range(q):
    l, r = LI_()
    n = l % d
    print(C[n][r // d] - C[n][l // d])
