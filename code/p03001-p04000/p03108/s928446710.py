# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:59:59 2019

@author: Yamazaki Kenichi
"""

N,M = map(int,input().split())
bb = [list(map(int,(input().split()))) for i in range(M)]

def comb2(N):
    return N*(N-1)//2
ans = [int(comb2(N))]
bb.reverse()

T = [[-1,1] for i in range(N+1)]
def p(u):
    return T[u][0]
def findset(u):
    if p(u) == -1:
        return u
    else:
        T[u][0] = findset(p(u))
        return T[u][0]
def unite(u,v):
    if findset(u) == findset(v):
        return    
    if T[findset(u)][1] >= T[findset(v)][1]:
        T[findset(u)][1] += T[findset(v)][1]
        T[findset(v)][0] = findset(u)
    else:
        T[findset(v)][1] += T[findset(u)][1]
        T[findset(u)][0] = findset(v)
        
for c in bb:
    if findset(c[0]) != findset(c[1]):
        res1 = T[findset(c[0])][1]
        res2 = T[findset(c[1])][1]
        unite(c[0],c[1])
        ans.append(ans[-1]-res1*res2)
    else:
        ans.append(ans[-1])
for i in range(M):
    print(ans[-i-2])
