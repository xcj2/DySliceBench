
rank = []
p = []


def makeSet(x):
    p.append(x)
    rank.append(0)


def union(x, y):
    link(findSet(x), findSet(y))


def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] = rank[y] + 1


def findSet(x):
    if x != p[x]:
        p[x] = findSet(p[x])
    return p[x]


def same(x, y):
    return findSet(x) == findSet(y)

def kruskal(g):
    MST = 0
    edges = g

    for e in edges:
        u = e[0]
        v = e[1]


        if findSet(u) != findSet(v):
            union(u, v)
            MST += e[2]

    return MST


V, E = map(int, input().split())
G = [list(map(int, input().split())) for i in range(E)]
G.sort(key=lambda x: x[2])

for i in range(V):
    makeSet(i)

print(kruskal(G))

