N,M = map(int,input().split())

par = [-1]*(N+1)


def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True


def same(x,y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]

A = [0]*M
B = [0]*M
for i in range(M):
    A[i], B[i] = map(int,input().split())


ans = [0]*M
ans[-1] = N*(N-1)//2
for j in range(M-1,0,-1):
    if same(A[j],B[j]):
        ans[j-1] = ans[j]

    else:
        sa = size(A[j])
        sb = size(B[j])
        ans[j-1] = ans[j] - sa*sb
    unite(A[j], B[j])

for i in range(M):
    print(ans[i])