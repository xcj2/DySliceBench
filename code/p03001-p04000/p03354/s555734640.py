def main():
    N, M = (int(i) for i in input().split())
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
    P = [int(i)-1 for i in input().split()]
    for i in range(M):
        x, y = (int(i)-1 for i in input().split())
        unite(x, y)
    ans = 0
    for i, p in enumerate(P):
        if is_same_group(i, p):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
