N, M, K = map(int, input().split())
par = list(range(N))
siz = [1] * N
n_friend = [0] * N


def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]


def same(x, y):
    return root(x) == root(y)


def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if siz[x] > siz[y]:
        x, y = y, x
    siz[y] += siz[x]
    par[x] = y


def tree_size(x):
    return siz[root(x)]


B = {}
for i in range(N):
    B[i] = set()
for _ in range(M):
    p, q = map(int, input().split())
    n_friend[p - 1] += 1
    n_friend[q - 1] += 1
    unite(p - 1, q - 1)
for _ in range(K):
    p, q = map(int, input().split())
    B[p - 1].add(q - 1)
    B[q - 1].add(p - 1)


# calc friend candidate
i, blocked = 0, 0
for b in B[0]:
    if same(i, b):
        blocked += 1
print(tree_size(i) - 1 - n_friend[i] - blocked, end='')
for i in range(1, N):
    print(' ', end='')
    blocked = 0
    for b in B[i]:
        if same(i, b):
            blocked += 1
    print(tree_size(i) - 1 - n_friend[i] - blocked, end='')
print('')
