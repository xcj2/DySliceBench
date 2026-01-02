from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from copy import deepcopy

INF = 10 ** 20
sys.setrecursionlimit(2147483647)

def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7

n,m=LI()
G=[[]for _ in range(n)]
cnt=[0]*n
for _ in range(n-1+m):
    a,b=LI()
    G[a-1]+=[b-1]
    cnt[b-1]+=1

r=cnt.index(0)
D=[0]*n
q=deque([r])
ans=[0]*n
while q:
    u=q.popleft()
    for v in G[u]:
        cnt[v]-=1
        ans[v] = u + 1
        if not cnt[v]:
            q+=[v]


print(*ans,sep="\n")






