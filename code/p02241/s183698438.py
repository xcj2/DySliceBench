def main():
    N = int(input())
    c = [[int(i) for i in input().split()] for j in range(N)]
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            if c[i][j] != -1:
                edges.append((c[i][j], (i, j)))
    edges.sort()

    par = [i for i in range(N)]
    rank = [0 for i in range(N)]

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
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    ans = 0
    for c, e in edges:
        if find_root(e[0]) != find_root(e[1]):
            unite(e[0], e[1])
            ans += c
    print(ans)


if __name__ == '__main__':
    main()

