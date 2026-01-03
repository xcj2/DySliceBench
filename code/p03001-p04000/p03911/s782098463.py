N, M = [int(_) for _ in input().split()]
KL = [[int(_) for _ in input().split()] for _ in range(N)]

UF = list(range(M + 1))


def find(a, x):
    if a[x] != x:
        a[x] = find(a, a[x])
    return a[x]


def unite(a, x, y):
    x = find(a, x)
    y = find(a, y)
    a[x] = a[y] = min(x, y)


def same(a, x, y):
    return find(a, x) == find(a, y)


for kl in KL:
    K, L = kl[0], kl[1:]
    for i in range(K - 1):
        unite(UF, L[i], L[i + 1])
for kl in KL:
    if not same(UF, KL[0][1], kl[1]):
        print('NO')
        exit()
print('YES')
