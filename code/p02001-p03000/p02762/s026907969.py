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
    edge = [set() for _ in range(N)]
    for i in [0]*M:
        a, b = (int(i) for i in input().split())
        edge[a-1].add(b-1)
        edge[b-1].add(a-1)
        unite(a-1, b-1)
    from collections import Counter
    for i, x in enumerate(par):
        unite(i, x)
    c = Counter(par)  # 頂点iの連結成分のサイズ
    for i in [0]*K:
        a, b = (int(i) for i in input().split())
        if is_same_group(a-1, b-1):
            edge[a-1].add(b-1)
            edge[b-1].add(a-1)
    for i in range(N):
        cur = c[par[i]] - len(edge[i]) - 1
        print(cur, end=" ")
    print()


if __name__ == '__main__':
    main()
