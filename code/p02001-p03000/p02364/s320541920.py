v, e = map(int, input().split())

from heapq import heappush, heappop
edges = []
for _ in range(e):
    s, t, w = map(int, input().split())
    heappush(edges, (w, s, t))

# initialize
par = [-1] * v
rank = [0] * v
# Union Find Tree
def find(x):
    """ 根ノードの値を見つけて返す """
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    """xとyを結合する"""
    rootx = find(x)
    rooty = find(y)

    if rootx == rooty:
        return False
    else:
        if rank[rootx] < rank[rooty]:
            par[rootx] = rooty
        else:
            par[rooty] = rootx
            if rank[rootx] == rank[rooty]: rank[rootx] += 1
        return True

def same(x, y):
    """ xとyが同じ集合に属しているか """
    return find(x) == find(y)

ans = 0
while edges:
    w, s, t = heappop(edges)
    if not same(s, t):
        ans += w
        unite(s, t)

print(ans)

