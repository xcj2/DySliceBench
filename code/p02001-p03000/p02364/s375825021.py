par  =[]
V, E = [int(s) for s in input().split()]
for i in range(V+1):
    par.append(i)

graph = []

for _ in range(E):
    x, y, w = [int(s) for s in input().split()]
    graph.append((x,y,w))

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

graph = sorted(graph, key=lambda x: x[2])
ans = 0
for g in graph:
    if not same(g[0], g[1]):
        union(g[0], g[1])
        ans += g[2]
print(ans)




