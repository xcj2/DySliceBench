def main():
    N, M, K=map(int, input().split())
    friend_or_block = [0] * N
    parent = [-1] * N

    def root(x):
        p, s = parent[x], list()
        while p >= 0:
            s.append(x)
            x, p = p, parent[p]
        for c in s: parent[c] = x
        return x

    def same(x, y): return root(x) == root(y)

    def count(x): return -parent[root(x)]

    def unite(x, y):
        xr, yr = root(x), root(y)
        if xr == yr: return
        if parent[xr] > parent[yr]: xr, yr = yr, xr
        parent[xr] += parent[yr]
        parent[yr] = xr

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        unite(a, b)
        friend_or_block[a] += 1
        friend_or_block[b] += 1

    for _ in range(K):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        if same(c, d):
            friend_or_block[c] += 1
            friend_or_block[d] += 1

    print(*[count(i) - friend_or_block[i] - 1 for i in range(N)])

if __name__ == '__main__':
    main()

