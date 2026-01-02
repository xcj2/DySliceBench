# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:29:39 2019

@author: Yamazaki Kenichi
"""

H,W = map(int,input().split())
A = [input() for i in range(H)]
T = [[-1,0,0] for j in range(H*W)] 

def g(x,i,j):
    if x == '.':
        return 1 if (i+j)%2 == 0 else 2
    else:
        return 4 if (i+j)%2 == 0 else 3
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
#    if T[findset(u)[0]][findset(u)[1]][1]+T[findset(u)[0]][findset(u)[1]][0
#         ] >= T[findset(v)[0]][findset(v)[1]][0]+T[findset(v)[0]][findset(v)[1]][1]:
    T[findset(u)][1] += T[findset(v)][1]
    T[findset(u)][2] += T[findset(v)][2]
    T[findset(v)][0] = findset(u)
def unite_check(i1,j1,i2,j2):
    if g(A[i1][j1],i1,j1)%2 == 0 and g(A[i2][j2],i2,j2)%2 == 0:
        unite(i1 * W + j1, i2 * W + j2)
    elif g(A[i1][j1],i1,j1)%2 == 1 and g(A[i2][j2],i2,j2)%2 == 1:
        unite(i1 * W + j1, i2 * W + j2)

for i in range(H):
    for j in range(W):
        if g(A[i][j],i,j) <= 2:
            T[i * W + j][1] += 1
        else:
            T[i * W + j][2] += 1
        if i !=0:
            unite_check(i,j,i-1,j)
        if j !=0:
            unite_check(i,j,i,j-1)
ans = 0
for i in range(H):
    for j in range(W):
        if T[i * W + j][0] == -1:
            ans += T[i * W + j][1] * T[i * W + j][2]
print(ans)
