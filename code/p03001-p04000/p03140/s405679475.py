# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n = II()
src = [SI() for _ in range(3)]

ans = 0
for i in range(n):
    tmp = set()
    for c in src:
        tmp.add(c[i])
    if len(tmp) == 3:
        ans += 2
    elif len(tmp) == 2:
        ans += 1

print(ans)
