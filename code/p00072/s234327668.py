def kruskal(n: int, edges: list) -> int:
    tree = [-1]*n

    def get_root(x):
        if tree[x] < 0:
            return x
        else:
            tree[x] = get_root(tree[x])
            return tree[x]

    def unite(x, y):
        x, y = get_root(x), get_root(y)
        if x != y:
            big, small = (x, y) if tree[x] < tree[y] else (y, x)
            tree[big] += tree[small]
            tree[small] = big
        return x != y

    edges.sort()
    total = 0
    cnt = 0
    for w, s, t in edges:
        if unite(s, t):
            cnt += 1
            total += w
            if cnt == n - 1:
                break

    return total

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
