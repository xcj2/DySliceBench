import sys

def kruskal(n: int, edges: list) -> int:
    tree = [-1]*n

    def get_root(x):
        if tree[x] < 0:
            return x
        tree[x] = get_root(tree[x])
        return tree[x]

    def unite(x, y):
        x, y = get_root(x), get_root(y)
        if x != y:
            big, small = (x, y) if tree[x] < tree[y] else (y, x)
            tree[big] += tree[small]
            tree[small] = big
        return x != y

    return sum(w for (w, _, _), _ in zip(filter(lambda p: unite(p[1], p[2]), sorted(edges)), range(n-1)))

V, E = map(int, input().split())
edges = [(w, s, t) for s, t, w in (map(int, l.split()) for l in sys.stdin)]
print(kruskal(V, edges))
