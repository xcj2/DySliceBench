import sys
N, M = map(int, sys.stdin.readline().rstrip().split(" "))
bridges = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    a, b = a - 1, b - 1
    bridges.append((a,b))

par = []
# for i in range(N):
#     par[i] = i

# siz = [1] * N

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

    # if siz[tmpx] <= siz[tmpy]:
    #     tmpx, tmpy = tmpy, tmpx
    # siz[tmpx] += siz[tmpy]

    par[tmpy] = tmpx

ans = 0
for i in range(M):
    par = [k for k in range(N)]
    for j, e in enumerate(bridges):
        if j == i:
            continue
        a, b = e
        unite(a, b)

    a, b = bridges[i]
    if not issame(a, b):
        ans += 1

print(ans)
