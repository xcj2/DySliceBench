import sys

def kruskal(v_count: int, edges: list) -> int:
    tree = [-1]*v_count

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

    cost = 0
    for (w, _s, _t), _ in zip(filter(lambda p: unite(*p[1:]), sorted(edges)),
                              range(v_count-1)):
        cost += w
    return cost

V, E = map(int, input().split())
edges = [(w, s, t) for s, t, w in (map(int, l.split()) for l in sys.stdin)]
print(kruskal(V, edges))
