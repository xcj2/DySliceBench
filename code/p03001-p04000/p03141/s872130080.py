# coding:utf-8

import sys
import heapq
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n = II()
src = []
for i in range(n):
    a, b = LI()
    src.append((a + b, a, b))
src.sort()


# print(*src, sep='\n')


score_a, score_b = 0, 0
for i in range(n):
    if i % 2:
        x, a, b = src.pop()
        score_b += b

    else:
        x, a, b = src.pop()
        score_a += a

print(score_a - score_b)
