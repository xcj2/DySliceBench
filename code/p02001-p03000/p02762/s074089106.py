def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M, K = (int(i) for i in input().split())
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
    fre = [set() for _ in range(N)]
    blo = [set() for _ in range(N)]
    mem = {i for i in range(N)}
    for i in [0]*M:
        a, b = (int(i) for i in input().split())
        fre[a-1].add(b-1)
        fre[b-1].add(a-1)
        unite(a-1, b-1)
    cur = [-1]*N
    from collections import Counter
    for i, x in enumerate(par):
        unite(i, x)
    c = Counter(par)
    # print(par, is_same_group(5, 7))
    for i in [0]*K:
        a, b = (int(i) for i in input().split())
        if is_same_group(a-1, b-1):
            blo[a-1].add(b-1)
            blo[b-1].add(a-1)
    for i in range(N):
        cur = c[par[i]] - len(fre[i]) - len(blo[i]) - 1
        print(cur, end=" ")
    print()


if __name__ == '__main__':
    main()
