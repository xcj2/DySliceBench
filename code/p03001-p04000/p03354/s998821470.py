#!/usr/bin/env python3


n,m = map(int,input().split())
p = list(map(int,input().split()))
for i in range(n):
    p[i] -= 1

#連結成分に属するかどうかを見るときはUnion-Findを用いる
#根(属するクラス)を返す関数
def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]
#同じクラスに属するかどうかを返す関数
def same(x,y):
    return root(x) == root(y)
#木を結合する関数
def union(x,y):
    x = root(x)
    y = root(y)
    #高さの高いほうに低いほうを結合
    if rank[x] < rank[y]:
        par[x] = y#xの親(属するクラス)をyとする
    else:
        par[y] = x
        if rank[x] == rank[y]:#高さが同じ場合
            rank[x] += 1#高さは1つ増える
par = [i for i in range(n)]
rank = [0 for _ in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    #swapできる頂点は同じ木にして同じ連結成分にする
    if not same(x-1,y-1):
        union(x-1,y-1)

ans = 0
for i in range(n):
    #p[i]とiが同じ連結成分ならばans+1
    if root(p[i]) == root(i):
        ans += 1
print(ans)
