import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

from bisect import bisect_right
from operator import itemgetter

N,M,Q = II()
x = []
for _ in range(M):
    L,R = II()
    x.append((L-1, R-1))
query = []
for _ in range(Q):
    p0,q0 = II()
    query.append((p0-1, q0-1))

x.sort(key=itemgetter(1))

y = [[10**5+1]*M for _ in range(N)]
c = [0]*N
for i in range(M):
    for j in range(x[i][0]+1):
        y[j][c[j]] = x[i][1]
        c[j] += 1

ans = 0
for q in query:
    print(bisect_right(y[q[0]], q[1]))