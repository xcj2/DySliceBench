def main():
    N, M = (int(i) for i in input().split())

    par = [i for i in range(N)]
    size = [1 for i in range(N)]

    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            size[x] = size[par[x]]
            return par[x]

    def same(x, y):
        return find(x) == find(y)

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        size[x] += size[y]
        par[y] = x

    def get_size(x):
        return size[find(x)]

    for _ in range(M):
        a, b = (int(i)-1 for i in input().split())
        union(a, b)

    ans = max(get_size(i) for i in range(N))

    print(ans)


if __name__ == '__main__':
    main()
