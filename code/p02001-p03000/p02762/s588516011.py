def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    if find(x) == find(y):
        return True
    else:
        return False

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

def uCnt(x):
    return -par[find(x)]

N, M, K = map(int, input().split())
par = [-1 for i in range(N + 1)]
rank = [0] * (N + 1)
frendCnt = [0] * (N + 1)
bloc = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    frendCnt[a] += 1
    frendCnt[b] += 1
    unite(a, b)

for i in range(K):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    bloc[c].append(d)
    bloc[d].append(c)

for i in range(N):
    ans = uCnt(i) - frendCnt[i] - 1
    for j in bloc[i]:
      if same(i, j):
           ans -= 1
    print(ans, end=' ')
