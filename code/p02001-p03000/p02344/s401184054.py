rank = []
p = []
w = []

def makeSet(x):
    p.append(x)
    rank.append(0)
    w.append(0)


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
    if p[x] == x:
        return x

    i = findSet(p[x])
    w[x] += w[p[x]]
    p[x] = i
    return i


def same(x, y):
    return findSet(x) == findSet(y)

def relate (x,y,z):
    i = findSet(x)
    j = findSet(y)

    if rank[i] < rank[j]:
        p[i] = j
        w[i] = z - w[x] + w[y]
    else:
        p[j] = i
        w[j] = -z - w[y] + w[x]
        if rank[i] == rank[j]:
            rank[i] += 1

n, q = map(int, input().split())
for i in range(n):
    makeSet(i)
for i in range(q):
    com, *cmd = map(int, input().split())
    if com == 0:
        relate(cmd[0], cmd[1],cmd[2])
    else:
        x, y = cmd
        if same(x, y):
            print(w[x] - w[y])
        else:
            print("?")

