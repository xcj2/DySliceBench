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
def Line(N,num):
    if N<=0:
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N,M = II()
p = []
S = []
for i in range(M):
    a,b = map(str, input().split())
    p.append(int(a))
    S.append(b)

ac = [False]*N
pn = [0]*N
acn = 0
pnn = 0

for i in range(M):
    if S[i]=='WA':
        pn[p[i]-1] += 1
    else:
        if ac[p[i]-1]==False:
            acn += 1
            ac[p[i]-1] = True
            pnn += pn[p[i]-1]

print(acn,pnn)