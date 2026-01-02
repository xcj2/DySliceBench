import sys
N, M = map(int, sys.stdin.readline().rstrip().split(" "))
bridges = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    a, b = a - 1, b - 1
    bridges.append((a,b))

par = [k for k in range(N)]
siz = [1] * N

def root(x):
    if par[x] == x:
        return x
    else:
        par[x] = root(par[x])
        return par[x]

def issame(x, y):
    return root(x) == root(y)

def unite(x, y):
    tmpx = root(x)
    tmpy = root(y)

    if tmpx == tmpy:
        return

    if siz[tmpx] <= siz[tmpy]:
        tmpx, tmpy = tmpy, tmpx
    siz[tmpx] += siz[tmpy]

    par[tmpy] = tmpx


# 不便さの初期値は橋が無い状態
Inconv = (N*(N-1)) // 2

ans = [0 for _ in range(M)]
ans[M-1] = Inconv

# print(bridges)

for i in reversed(range(1, M)):
    a, b = bridges[i]
    if not issame(a, b):
        Inconv -= siz[root(a)] * siz[root(b)]
    ans[i - 1] = Inconv
    unite(a, b)

for i in range(M):
    print(ans[i])
