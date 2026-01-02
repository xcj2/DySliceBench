# Union-Find
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    return True


def same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


N, M, K = map(int, input().split())
Friend = [[] for _ in range(N)]

par = [-1] * N
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    unite(a, b)
    Friend[a].append(b)
    Friend[b].append(a)

Block = [[] for _ in range(N)]
for i in range(K):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    Block[c].append(d)
    Block[d].append(c)

Ans = []
for i in range(N):
    ans = size(i) - 1
    ans -= len(Friend[i])
    for b in Block[i]:
        if same(i, b):
            ans -= 1
    Ans.append(str(ans))

print(' '.join(Ans))