def Find(x, par):
    if par[x] < 0:
        return x
    else:
        par[x] = Find(par[x], par)
        return par[x]

def Unite(x, y, par, rank):
    x = Find(x, par)
    y = Find(y, par)

    if x != y:
        if rank[x] < rank[y]:
            par[y] += par[x]
            par[x] = y
        else:
            par[x] += par[y]
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

def Same(x, y, par):
    return Find(x, par) == Find(y, par)

def Size(x, par):
    return -par[Find(x, par)]

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

par = [-1]* n
rank = [0]*n

C = [0]*n

for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    C[a] += 1
    C[b] += 1
    Unite(a, b, par, rank)

ans = [0]*n
for i in range(n):
    ans[i] = Size(i, par)-1-C[i]

for i in range(k):
    c, d = map(int, input().split())
    c, d = c-1, d-1
    if Same(c, d, par):
        ans[c] -= 1
        ans[d] -= 1

print(*ans)
