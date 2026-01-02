n, m = map(int, input().split())
P = tuple(map(lambda x: int(x)-1, input().split()))
par = list(range(n))
size = [1] * n
def find(x):
    """ 根のノードの値を見つけて返す """
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]

def unite(x, y):
    """xとyを結合する"""
    rootx = find(x)
    rooty = find(y)
    if rootx == rooty:
        return False
    else:
        if size[rootx] < size[rooty]:
            par[rootx] = rooty
            size[rooty] += size[rootx]
        else:
            par[rooty] = rootx
            size[rootx] += size[rooty]
        return True

def same(x, y):
    """ xとyが同じ集合に属しているか """
    return find(x) == find(y)

for _ in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    unite(x, y)
groups = {}
for idx, p in enumerate(par):
    p = find(p)
    groups.setdefault(p, set())
    groups[p].add(idx)

cnt = 0
for k, g in groups.items():
    for gi in g:
        pi = P[gi]
        if pi in g:
            cnt += 1
print(cnt)
