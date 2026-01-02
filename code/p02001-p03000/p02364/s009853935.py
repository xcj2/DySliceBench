import sys
from itertools import islice

def kruskal(v_count: int, edges: list) -> int:
    tree = [-1]*v_count

    def get_root(x):
        if tree[x] < 0:
            return x
        tree[x] = get_root(tree[x])
        return tree[x]

    def unite(a):
        x, y = get_root(a[1]), get_root(a[2])
        if x != y:
            big, small = (x, y) if tree[x] < tree[y] else (y, x)
            tree[big] += tree[small]
            tree[small] = big
        return x != y

    cost = 0
    for w, _s, _t in islice(filter(unite, sorted(edges)), v_count-1):
        cost += w
    return cost

V, E = map(int, input().split())
edges = [(w, s, t) for s, t, w in (map(int, l.split()) for l in sys.stdin)]
print(kruskal(V, edges))
