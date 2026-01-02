def main():
    N, M = (int(i) for i in input().split())
    par = [i for i in range(N)]
    rank = [1]*N

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

    ans = [N*(N-1)//2]
    AB = [[int(i)-1 for i in input().split()] for j in range(M)]
    for a, b in AB[::-1]:
        if is_same_group(a, b):
            ans.append(ans[-1])
        else:
            p = size(a)
            q = size(b)
            # print(a, b, p, q)
            unite(a, b)
            ans.append(ans[-1] - p * q)
    ans = ans[::-1]
    for a in ans[1:]:
        print(a)


if __name__ == '__main__':
    main()
