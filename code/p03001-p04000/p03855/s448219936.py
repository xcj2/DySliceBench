N, K, L = [int(_) for _ in input().split()]

par = [i for i in range(2 * N)]
rank = [0] * (2 * N)


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def same(x, y):
    return find(x) == find(y)


for _ in range(K):
    p, q = [int(_) - 1 for _ in input().split()]
    unite(p, q)
for _ in range(L):
    r, s = [int(_) + N - 1 for _ in input().split()]
    unite(r, s)
memo = {}
for i in range(N):
    memo[find(i), find(i + N)] = memo.get(
        (find(i), find(i + N)), 0) + 1

print(' '.join(str(memo[find(i), find(i + N)])
               for i in range(N)))
