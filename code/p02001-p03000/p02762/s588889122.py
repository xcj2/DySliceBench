def main():
    N, M, K = (int(i) for i in input().split())
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
        # 連結成分のサイズを返す
        return rank[find_root(x)]

    fri = [[] for _ in range(N)]
    for _ in range(M):
        a, b = (int(i) for i in input().split())
        fri[a-1].append(b-1)
        fri[b-1].append(a-1)
        unite(a-1, b-1)
    block = [[] for _ in range(N)]
    for i in range(K):
        a, b = (int(i) for i in input().split())
        if is_same_group(a-1, b-1):
            block[a-1].append(b-1)
            block[b-1].append(a-1)
    ans = []
    for i in range(N):
        cur = size(i) - len(fri[i]) - len(block[i]) - 1
        ans.append(cur)
    print(*ans)


if __name__ == '__main__':
    main()
