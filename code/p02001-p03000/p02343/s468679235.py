import sys
sys.setrecursionlimit(10**7)

n,q = [int(s) for s in input().split()]
par = []
for i in range(n):
    par.append(i)

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x,y):
    return find(x) == find(y)

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        par[x] = y

for i in range(q):
    q_type,x,y = [int(s) for s in input().split()]
    if q_type == 1:
        if same(x,y):
            print(1)
        else:
            print(0)
    else:
        union(x,y)
