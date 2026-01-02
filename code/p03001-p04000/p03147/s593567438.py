# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n = II()
H = LI() + [0]

ans = 0
state = 1
for i in range(max(H)):
    for h in H:
        if state:
            if h >= i + 1:
                state = 0
        else:
            if h < i + 1:
                ans += 1
                state = 1


print(ans)
