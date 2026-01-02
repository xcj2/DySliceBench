def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M, K = (int(i) for i in input().split())
    AB = [[int(i)-1 for i in input().split()] for j in range(M)]
    CD = [[int(i)-1 for i in input().split()] for j in range(K)]

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

    friends = [[] for _ in range(N)]
    blocks = [[] for _ in range(N)]
    for a, b in AB:
        friends[a].append(b)
        friends[b].append(a)
        unite(a, b)
    for c, d in CD:
        if is_same_group(c, d):
            blocks[c].append(d)
            blocks[d].append(c)
    for i in range(N):
        ans = size(i) - len(friends[i]) - len(blocks[i]) - 1
        print(ans, end=" " if i != N-1 else "\n")


if __name__ == '__main__':
    main()
