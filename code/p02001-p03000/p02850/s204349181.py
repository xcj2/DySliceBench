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
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed==False:
            pt[t[i]-1].append(s[i]-1)
    return pt

N = I()
a,b = Line(N-1,2)
d = defaultdict(int)

pt = edges_to_pt(a,b,N)
for i in range(N-1):
    x = min(a[i],b[i])
    y = max(a[i],b[i])
    d[(x-1)*N+(y-1)] = i

ans = [0]*(N-1)
used = [False]*N
used[0] = True

color = [0]*N
q = [0]
c = 1
while q:
    q1 = []
    for i in q:
        c = 1
        for j in pt[i]:
            if used[j]==False:
                if c==color[i]:
                    c += 1
                color[j] = c
                used[j] = True
                ans[d[min(i,j)*N+max(i,j)]] = c
                c += 1
                q1.append(j)
    q = q1

print(max(ans))
for i in range(N-1):
    print(ans[i])