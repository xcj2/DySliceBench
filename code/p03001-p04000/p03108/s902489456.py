N, M = map(int, input().split())
ils = [map(int, input().split()) for _ in range(M)]

par = [-1 for i in range(N)]

def root(x):
    if par[x] < 0:
        return x
    else:
        par[x] = root(par[x])
        return par[x]
        
def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if size(x) < size(y):
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    
def same(x, y):
    return root(x) == root(y)

def size(x):
    return - par[root(x)]
    
    
inconv = N * (N - 1) // 2
result = [0] * M
for i in range(M - 1, -1, -1):
    A, B = ils[i]
    A -= 1
    B -= 1
    result[i] = inconv
    if not same(A, B):
        inconv -= size(A) * size(B)
        unite(A, B)
    
for i in result:
    print(i)