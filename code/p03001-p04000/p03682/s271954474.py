import sys
sys.setrecursionlimit(10**7)


par  =[]
N = int(input())

graph = []

for i in range(N):
    x, y = [int(s) for s in input().split()]
    graph.append((i, x, y))

sort_x = sorted(graph, key=lambda x: x[1])
sort_y = sorted(graph, key=lambda x: x[2])

edges = []

for i in range(len(sort_x)-1):
    i1, a, b = sort_x[i]
    i2, c, d = sort_x[i+1]
    w = min(abs(a-c), abs(b-d))
    edges.append((i1, i2, w))
    i1, a, b = sort_y[i]
    i2, c, d = sort_y[i+1]
    w = min(abs(a-c), abs(b-d))
    edges.append((i1, i2, w))


for i in range(N+1):
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

ans = 0
edges = sorted(edges, key=lambda x: x[2])
for edge in edges:
    if not same(edge[0], edge[1]):
        union(edge[0], edge[1])
        ans += edge[2]
print(ans)



