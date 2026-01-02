def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return

    # sizeの大きいほうがx
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x


def same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


n, m, k = map(int, input().split())

par = [-1] * n
friend = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    union(a-1, b-1)
    friend[a-1] += 1
    friend[b-1] += 1

block = [[] for _ in range(n)]
for _ in range(k):
    c, d = map(int, input().split())
    block[c-1].append(d-1)
    block[d-1].append(c-1)

for i in range(n):
    ans = size(i) - friend[i] - 1
    for j in block[i]:
        if same(i, j):
            ans -= 1
    print(ans, end=' ')