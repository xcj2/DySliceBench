def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = (int(i) for i in input().split())

    par = [i for i in range(N)]
    rank = [1]*N
    weight = [0]*N

    def find_root(x):
        if par[x] == x:
            return x
        else:
            r = find_root(par[x])
            weight[x] += weight[par[x]]
            par[x] = r
            return par[x]

    def get_weight(x):
        find_root(x)
        return weight[x]

    def get_diff(x, y):
        return get_weight(y) - get_weight(x)

    def is_same_group(x, y):
        return find_root(x) == find_root(y)

    def unite(x, y, w):
        w += get_weight(x)
        w -= get_weight(y)
        x = find_root(x)
        y = find_root(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            x, y = y, x
            w = -w
        rank[x] += rank[y]
        par[y] = x
        weight[y] = w

    def size(x):
        # 連結成分のサイズを返す
        return rank[find_root(x)]

    for i in range(M):
        le, ri, d = (int(i) for i in input().split())
        le -= 1
        ri -= 1
        if is_same_group(le, ri):
            diff = get_diff(le, ri)
            if diff != d:
                return print("No")
        else:
            unite(le, ri, d)
    print("Yes")


if __name__ == '__main__':
    main()
