# Minimum Spanning Tree
p = []
rank = []
edge = []
cost = 0

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

[v, e] = list(map(int, input().split()))
for i in range(v):
    makeSet(i)

for i in range(e):
    [s, t, w] = list(map(int, input().split()))
    edge.append([w, s, t])

edge.sort()

while v > 1:
    min = edge.pop(0)
    if not same(min[1], min[2]):
        union(min[1], min[2])
        cost += min[0]
        v -= 1

print(cost)
