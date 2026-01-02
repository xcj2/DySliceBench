def init(n):
    par = list(range(n))
    size = [1] * n
    return par, size

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
    if size[x] < size[y]:
        par[x] = y
        size[y] += size[x]
    else:
        par[y] = x
        size[x] += size[y]


N, M, K = map(int, input().split())

par, size = init(N+1)
non_candidates = [1] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    unite(a, b)
    non_candidates[a] += 1
    non_candidates[b] += 1
    

for i in range(K):
    c, d = map(int, input().split())
    if same(c, d):
        non_candidates[c] += 1
        non_candidates[d] += 1

for i in range(1, N+1):
    print(size[root(i)] - non_candidates[i], end=" ")
    # print(i, size[root(i)], non_candidates[i])
    