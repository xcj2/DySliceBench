# -*- coding: utf-8 -*-
# D - Decayed Bridges
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

N,M = map(int,readline().split())
#0-index
par = [-1]*N
query = []
for _ in range(M):
    x,y = map(int,readline().split())
    query.append((x-1,y-1))

ans = [N*(N-1)//2]
for i in range(M-1):
    x,y = query[-(i+1)]
    a = ans[-1]
    if same(x,y) == False:
        a = ans[-1]-size(x)*size(y)
    ans.append(a)
    if a == 0:
        break
    union(x,y)
S = len(ans)
for i in range(M-S):
    ans.append(0)

print(*ans[::-1],sep='\n')