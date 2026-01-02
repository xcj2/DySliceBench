import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# # input = sys.stdin.readline
# sys.setrecursionlimit(10**8)
# mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n,k = inpm()
P = [0] + inpl()
C = [0] + inpl()

ans = 1000000010 * -1
for start in range(1,n+1):
    l = [0] * (n+1)
    l[start] = 1
    now = start
    score = []
    while True:
        l[now] = 1
        score.append(C[P[now]])
        if l[P[now]] == 1:
            break
        now = P[now]
    
    ruiseki = []
    for i in range(len(score)):
        if i == 0:
            ruiseki.append(score[i])
        else:
            ruiseki.append(ruiseki[i-1] + score[i])

    a = ruiseki[-1] #1ループでのスコア
    b = max(ruiseki) #1ループ中の最大スコア
    c = k // len(ruiseki) #ループ可能回数
    d = k % len(ruiseki) #ループ抜けてからのあまり回数

    tmp = 0
    if c == 0:
        tmp = max(ruiseki[:d])
    elif c > 0:
        if a <= 0:
            tmp = b
        elif d == 0:
            tmp = a*(c-1) + b
        else:
            tmp = max(a*c + max(ruiseki[:d]),a*(c-1) + b)
    ans = max(ans,tmp)

print(ans)