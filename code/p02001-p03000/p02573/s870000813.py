# -*- coding: utf-8 -*-
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

#Union Find
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
#xとyの属する集合の併合
def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y] #xにyの個数くっつける 
        par[y] = x #yをxにくっつける
        return 

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

N,Q = map(int,readline().split())
#0-index
par = [-1]*(N+1)
for _ in range(Q):
    x,y = map(int,readline().split())
    union(x,y)

print(-min(par))