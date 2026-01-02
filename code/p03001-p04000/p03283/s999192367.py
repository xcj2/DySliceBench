# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, m, q = LI()

train = [[0] * n for _ in range(n)]
for _ in range(m):
    l, r = LI_()
    train[n - 1 - l][r] += 1

for i in range(n):
    for j in range(1, n):
        train[i][j] += train[i][j - 1]

for j in range(n):
    for i in range(1, n):
        train[i][j] += train[i - 1][j]

for _ in range(q):
    a, b = LI_()
    print(train[n - 1 - a][b])
