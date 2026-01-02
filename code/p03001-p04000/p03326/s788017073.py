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

from itertools import product

N,M = II()
x,y,z = Line(N)

a = [[0]*N for _ in range(8)]
p = list(product(['1','-1'],repeat=3))

for i,p0 in enumerate(p):
    for j in range(N):
        a[i][j] = eval(p0[0])*x[j]+eval(p0[1])*y[j]+eval(p0[2])*z[j]

for i in range(8):
    a[i].sort(reverse=True)

ans = -float('inf')
for i in range(8):
    temp = sum(a[i][:M])
    if temp>ans:
        ans = temp

print(ans)