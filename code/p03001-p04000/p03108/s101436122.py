# solution

import sys
input = sys.stdin.readline

def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

def unite(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        if rank[x] < rank[y]:
            par[x] = y
            size[y] += size[x]
        else:
            par[y] = x
            size[x] += size[y]
            if rank[x] == rank[y]:
                rank[x] += 1

def same(x, y):
    return find(x) == find(y)

N, M = map(int, input().split())

par = [0] * N
for i in range(N):
    par[i] = i

rank = [1] * N
size = [1] * N
res = []

edge2 = [[0] for i in range(M)]
for i in range(M):
    edge2[i] = list(map(int, input().split()))

edge = [[0] for i in range(M)]
for i in range(M):
    edge[i] = [edge2[M - 1 - i][0] - 1, edge2[M - 1 - i][1] - 1]

for i in range(M):
    fi = find(edge[i][0])
    se = find(edge[i][1])

    if fi == se:
        res.append(0)
    else:
        res.append(size[fi] * size[se])
        unite(fi, se)

ans = 0
for i in range(M):
    ans += res[M - 1 - i]
    print(ans)