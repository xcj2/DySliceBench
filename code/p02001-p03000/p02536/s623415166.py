import sys
sys.setrecursionlimit(10**9)

def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x,y):
    x, y = find(x), find(y)
    if x == y:
        return False
    
    if par[x] > par[y]:
        x,y = y,x
    par[x] += par[y]
    par[y] = x
    return True

def size(x):
    return -par[find(x)]

n, m = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append([a-1, b-1])

par = [-1]*n

for a, b in ab:
    unite(a, b)

nset=set()
for i in range(n):
    if not find(i) in nset:
        nset.add(find(i))
else:
    print(len(nset)-1)
    