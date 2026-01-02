[p, rank] = [[], []]
[n, q] = list(map(int, input().split()))
w = [0 for i in range(n)]

def findSet(x):
    global p
    if x != p[x]:
        pre_parent = p[x]
        p[x] = findSet(p[x])
        w[x] += w[pre_parent]
    return p[x]

def makeSet(x):
    global p, rank
    p.append(x)
    rank.append(0)


def link(x, y, z):
    global p, rank, w
    if rank[x] > rank[y]:
        p[y] = x
        w[y] = z
    else:
        p[x] = y
        w[x] = -z
        if rank[x] == rank[y]:
            rank[y] += 1

def relate(x, y, z):
    global w
    root_x = findSet(x)
    root_y = findSet(y)
    z += w[x]
    z -= w[y]
    link(root_x, root_y, z)

def same(x, y):
    if findSet(x) == findSet(y):
        return 1
    else:
        return 0   
   
def difference(x, y):
    if same(x, y) == 1:
        global w
        return w[y] - w[x]
    else:
        return "?"     

for i in range(n):
    makeSet(i)

for i in range(q):
    data = list(map(int, input().split()))
    if data[0] == 0:
        relate(data[1], data[2], data[3])
    else:
        print(difference(data[1], data[2]))

