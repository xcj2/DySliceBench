def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = (int(i) for i in input().split())
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

    for i in range(M):
        a, b, _ = (int(i)-1 for i in input().split())
        unite(a, b)
    ans = set()
    for i in range(N):
        ans.add(find_root(i))
    print(len(ans))


if __name__ == '__main__':
    main()
