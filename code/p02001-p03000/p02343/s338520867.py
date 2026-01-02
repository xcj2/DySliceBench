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


n, q = map(int, input().split())
for i in range(n):
    makeSet(i)
for i in range(q):
    com, x, y = map(int, input().split())

    if com == 0:
        union(x, y)
    elif com == 1:
        print(int(same(x, y)))
