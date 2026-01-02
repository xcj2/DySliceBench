import sys
sys.setrecursionlimit(10000)

def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def unite(x, y):
    rx = root(x)
    ry = root(y)
    if rx != ry:
        par[rx] = ry

def same(x, y):
    return root(x) == root(y)

n, m = map(int, input().split())
E = []
for i in range(m):
    s, t, w = map(int, input().split())
    E.append([w, s, t])

E.sort()

par = [i for i in range(n)]

ans = 0

for e in E:
    if not same(e[1], e[2]):
        unite(e[1], e[2])
        ans += e[0]

print(ans)
