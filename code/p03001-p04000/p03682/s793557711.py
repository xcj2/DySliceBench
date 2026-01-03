def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    XY = [[int(i) for i in input().split()] for j in range(N)]
    X = sorted([(xy[0], xy[1], i) for i, xy in enumerate(XY)])
    Y = sorted(X, key=lambda p: p[1])
    edges = []
    for i in range(N-1):
        (x1, y1, a) = X[i]
        (x2, y2, b) = X[i+1]
        cost = min(abs(x1-x2), abs(y1-y2))
        edges.append((cost, a, b))

    for i in range(N-1):
        (x1, y1, a) = Y[i]
        (x2, y2, b) = Y[i+1]
        cost = min(abs(x1-x2), abs(y1-y2))
        edges.append((cost, a, b))

    par = [i for i in range(N)]
    rank = [1 for i in range(N)]

    def find_root(x):
        if par[x] == x:
            return x
        else:
            par[x] = find_root(par[x])
            return par[x]

    def is_same_group(x, y):
        return find_root(x) == find_root(y)

    def unite(x, y):
        x = find_root(x)
        y = find_root(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            x, y = y, x
        rank[x] += rank[y]
        par[y] = x

    def size(x):
        return rank[find_root(x)]

    edges.sort()

    ans = 0
    for (c, a, b) in edges:
        if find_root(a) != find_root(b):
            ans += c
            unite(a, b)
    print(ans)


if __name__ == '__main__':
    main()
