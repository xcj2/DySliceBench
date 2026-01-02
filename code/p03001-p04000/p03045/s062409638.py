def uf_init(n):
    return list(range(n))

def uf_root(uf, x):
    update_node_arr = []
    while(uf[x] != x):
        update_node_arr.append(x)
        x = uf[x]
    for y in update_node_arr:
        uf[y] = x
    return x

def uf_same(uf, x, y):
    return uf_root(uf, x) == uf_root(uf, y)

def uf_unite(uf, x, y):
    x = uf_root(uf, x)
    y = uf_root(uf, y)
    if x == y:
        return
    uf[x] = y

N,M = (int(x) for x in input().split())

uf = uf_init(N)

for _ in range(M):
    X,Y,Z = (int(x) for x in input().split())
    uf_unite(uf, X-1, Y-1)

uf_roots = set()
for i in range(N):
    uf_roots.add(uf_root(uf, i))

print(len(uf_roots))

