rank = {}
p = {}

class Edge: pass

def makeSet(x):
    p[x] = x
    rank[x] = 0
 
def link(x, y):
    if  rank[x] > rank[y]: p[y] = x
    else: p[x] = y
    if  rank[x] == rank[y]:
        rank[y] += 1
 
def union(x, y):
    link(findSet(x), findSet(y))
     
def findSet(x):
    if  x != p[x]: p[x] = findSet(p[x])
    return p[x]
     
def isSameSet(x, y):
    return findSet(x) == findSet(y)
 
V, E = map(int, input().split())
el = []

for i in range(E):
    s,t,w = map(int, input().split())
    e=Edge()
    e.source = s
    e.target = t
    e.weight = w
    el.append(e)

def kruskal(v, e):
    e = sorted(e, key=lambda x: x.weight)
    for i in v:
        makeSet(i)
    K = []
    for i in e:
        if findSet(i.source) != findSet(i.target):
            union(i.source, i.target)
            K.append(i.weight)
    return K

print(sum(kruskal(range(V), el)))