def Find(x, par):
    if par[x] < 0:
        return x
    else:
        par[x] = Find(par[x], par)
        return par[x]

def Unite(x, y, par, rank):
    x = Find(x, par)
    y = Find(y, par)

    if x != y:
        if rank[x] < rank[y]:
            par[y] += par[x]
            par[x] = y
        else:
            par[x] += par[y]
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

def Same(x, y, par):
    return Find(x, par) == Find(y, par)

def Size(x, par):
    return -par[Find(x, par)]

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

par = [-1]* n
rank = [0]*n

for i in range(m):
    a,b = map(int, input().split())
    a, b =a-1, b-1
    Unite(a,b,par,rank)

cnt = 0
for i in range(n):
    if par[i] < 0:
        cnt += 1
print(cnt-1)
