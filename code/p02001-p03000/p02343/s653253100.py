# Disjoint Set: Union Find Tree
p = []
rank = []

def makeSet(x):
    global p, rank
    p.append(x)
    rank.append(0)

def findSet(x):
    global p
    if x != p[x]:
        p[x] = findSet(p[x])
    return p[x]

def link(x, y):
    global p, rank
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def union(x, y):
    link(findSet(x), findSet(y))    

def same(x, y):
    if findSet(x) == findSet(y):
        return 1
    else:
        return 0   

[n, q] = list(map(int, input().split()))
for i in range(n):
    makeSet(i)

for i in range(q):
    [com, x, y] = list(map(int, input().split()))
    if com == 0:
        union(x, y)
    else:
        print(same(x, y))
