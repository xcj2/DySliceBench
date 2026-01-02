n, q = map(int, input().split())
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

for _ in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        unite(u, v)
    else:
        print(int(same(u, v)))
