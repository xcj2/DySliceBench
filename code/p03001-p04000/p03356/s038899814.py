def main():
    N, M = (int(_) for _ in input().split())
    P = [int(_) for _ in input().split()]
    swap = [[int(_) for _ in input().split()] for __ in range(M)]

    par = [i for i in range(N+1)]
    rank = [0] * (N+1)

    # 要素xの親ノードを返す
    def find(x):
        if par[x] == x:
            return x
        par[x] = find(par[x])
        return par[x]

    # 要素x, yの属する集合を併合
    def unite(x, y):
        x, y = find(x), find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        return

    # xとyが同じ集合に属するか？
    def same(x, y):
        return find(x) == find(y)

    for a, b in swap:
        unite(a, b)

    ret = 0
    for i, p in enumerate(P, 1):
        if same(i, p): ret += 1
    print(ret)
    return

if __name__ == '__main__':
    main()
