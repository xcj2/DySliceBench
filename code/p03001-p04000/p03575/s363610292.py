N,M = map(int,input().split())
src = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(M)]

parent = [i for i in range(N)]
rank = [0] * N
def root(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = root(parent[a])
        return parent[a]
def is_same(a,b):
    return root(a) == root(b)
def unite(a,b):
    ra = root(a)
    rb = root(b)
    if ra == rb: return
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    else:
        parent[rb] = ra
        if rank[ra] == rank[rb]: rank[ra] += 1

ans = 0
for i in range(M):
    parent = [i for i in range(N)]
    rank = [0] * N
    for j,(a,b) in enumerate(src):
        if i == j: continue
        unite(a,b)
    if len(set([root(i) for i in range(N)])) > 1:
        ans += 1
print(ans)
