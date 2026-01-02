N, M = map(int, input().split())
ls = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

# Union Find Tree
def find(par, x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par, par[x])
        return par[x]

def unite(par, rank, x, y):
    rx = find(par, x)
    ry = find(par, y)

    if rx == ry:
        return False
    else:
        if rank[rx] < rank[ry]:
            par[rx] = ry
        else:
            par[ry] = rx
            if rank[rx] == rank[ry]: rank[rx] += 1
        return True

def same(par, x, y):
    return find(par, x) == find(par, y)

c = 0
for i in range(M):
    par = [-1] * N
    rank = [0] * N
    for idx, (a, b) in enumerate(ls):
        if idx == i:
            continue
        unite(par, rank, a, b)
    
    # グループが2つ以上ならばカウント
    if len([i for i, x in enumerate(par) if x < 0]) >= 2:
        c += 1
print(c)
