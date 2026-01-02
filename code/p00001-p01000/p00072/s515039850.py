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

    return sum(w for (w, _, _), _ in zip(filter(lambda p: unite(p[1], p[2]), sorted(edges)), range(n)))

while True:
    n = int(input())
    if not n:
        break
    m = int(input())
    inf = float("inf")

    edges = []
    for _ in [None]*m:
        s, t, d = map(int, input().split(","))
        edges.append((d//100-1, s, t))

    print(kruskal(n, edges))
