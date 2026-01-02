n = int(input())
G = [[int(i) for i in input().split()] for i in range(n)]

S = set([])
for i,row in enumerate(G):
    for j,col in enumerate(row):
        if col != -1:
            k = tuple(sorted([i,j]))
            S.add(k + (col, ))

rank = {}
p = {}

def makeSet(x):
    p[x] = x
    rank[x] = 0

def link(x, y):
    if  rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
    if  rank[x] == rank[y]:
        rank[y] += 1

def union(x, y):
    link(findSet(x), findSet(y))
    
def findSet(x):
    if  x != p[x]:
        p[x] = findSet(p[x])
    return p[x]
    
def isSameSet(x, y):
    return findSet(x) == findSet(y)

def kruskal(G, n, S):
    ret = 0
    for x in range(n):
        makeSet(x)
    while len(S) != 0:
        u, v, c = min(S, key=lambda x: x[2])
        S = S - set([(u,v,c)])
        if not isSameSet(u, v):
            union(u, v)
            ret += c
    return ret
print(kruskal(G, n, S))