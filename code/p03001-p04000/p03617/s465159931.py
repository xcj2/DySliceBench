# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


# 1, 2, 4, 8
amount = [4 * x for x in LI()]
n = I() * 4

performance = [(amount[i] // (2 ** i), i) for i in range(4)]
performance.sort()

bought_tea, fee = 0, 0
for i in range(4):
    tea = performance[i][1]
    litre = 2 ** tea
    q = (n - bought_tea) // litre
    bought_tea += q * litre
    fee += q * amount[tea]

print(fee // 4)
