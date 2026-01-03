
def kruskal(v_count: int, edges: list) -> int:
    """
    :param v_count: 頂点数
    :param edges: [(weight, from, to), ... ]
    """
    from itertools import islice
    tree = [-1]*v_count

    def get_root(x) -> int:
        if tree[x] < 0:
            return x
        tree[x] = get_root(tree[x])
        return tree[x]

    def unite(a) -> bool:
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

import sys
from operator import itemgetter
N = int(input())
#a = [[i]+list(map(int, l.split())) for i, l in enumerate(sys.stdin)]
a = []
for i in range(N):
  ta,tb =map(int,input().split())
  a.append([i,ta,tb])

x_sorted, y_sorted = sorted(a, key=itemgetter(1)), sorted(a, key=itemgetter(2))
edges = []
append = edges.append
for (i, x1, y1), (j, x2, y2) in zip(x_sorted, x_sorted[1:]):
    append((x2-x1, i, j))
for (i, x1, y1), (j, x2, y2) in zip(y_sorted, y_sorted[1:]):
    append((y2-y1, i, j))
#print(edges)
print(kruskal(N, edges))
