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

H,W = II()
S = [list(map(str, input())) for _ in range(H)]

def bfs(c,s):
    X=[[-1]*W for i in range(H)]
    if c[s[0]][s[1]]=='#':
        return X
    X[s[0]][s[1]]=0
    q=[s]
    counter=1
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    #f = float('inf')
    while q:
        q1=[]
        for i in q:
            for d0 in d:
                j = (i[0]+d0[0],i[1]+d0[1])
                if 0<=j[0]<=H-1 and 0<=j[1]<=W-1:
                    if c[j[0]][j[1]]=='.':
                        #if j[0]==g[0] and j[1]==g[1]:
                        #    f = min(f,counter)
                        if X[j[0]][j[1]]==-1:
                            X[j[0]][j[1]]=counter
                            q1.append(j)
        q=q1
        counter+=1
    return X

ans = 0
for si in range(H):
    for sj in range(W):
        d = bfs(S,(si,sj))
        #print(d)
        now = 0
        for i in range(len(d)):
            for j in range(len(d[0])):
                if d[i][j]>now:
                    now = d[i][j]
        if now==-1:
            continue
        if now>ans:
            ans = now
print(ans)