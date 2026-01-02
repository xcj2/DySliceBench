def makeSet(x):
    p[x] = x
    rank[x] = 0

def union(x, y):
    link(findSet(x), findSet(y))

def link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def findSet(x):
    if x != p[x]:
        p[x] = findSet(p[x])
    return p[x]

n,q = map(int, input().split())
p = [0]*n
rank = [0]*n

for x in range(n):
    makeSet(x)

for _ in range(q):
    com, x, y = map(int, input().split())
    if com==0:    
        union(x, y)
    else:
        if findSet(x)==findSet(y):
            print('1')
        else:
            print('0')


