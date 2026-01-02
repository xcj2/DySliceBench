import numpy as np

def find(x):
    if x == root[x]: return x
    else: root[x] = find(root[x]); return root[x]
def unite(x,y):
    px,py = find(x),find(y)
    if px == py : return
    else: root[px] = py
def same(x,y): return find(x)==find(y)


n,m = map(int,input().split())
ab = np.array([list(map(int,input().split())) for i in range(m)])
a,b = ab.T[0] -1, ab.T[1] -1

ans = 0
for i in range(m): #除外する辺を決める
    connect = 0
    root = list(range(n))
    for j in range(m): #i以外の辺についてuniteしていく
        if i != j and  not same(a[j],b[j]):
            unite(a[j],b[j]) ; connect += 1
    ans += 0 if connect == n-1 else 1
print(ans)


