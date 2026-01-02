# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n = II()
F = [LI() for _ in range(n)]
P = [LI() for _ in range(n)]

ans = -INF
for bit in range(1, 1024):
    profit = 0
    for shop in range(n):
        cnt = 0
        for shift in range(10):
            if not bit >> shift & 1:
                continue

            if F[shop][shift]:
                cnt += 1

        profit += P[shop][cnt]

    ans = max(ans, profit)

print(ans)
